# coding=utf-8
# pylint: disable=W0401,W0614,E0602

import pycaitlyn as pc
import pycaitlynutils3 as pcu3
import pycaitlynts3 as pcts3
import numpy as np


use_raw = True
# _debug = True
exports = {}

overwrite = True
# map_same_commodity = True

granularity = 60

push_interval = 0.5

# dynamic_load_balance = True
output_meta = None

outputs = {}

metas = {}

imports = {}


class SampleQuote(pcts3.sv_object):
    '''
    Python wrapper for global::SampleQuote
    '''
    instance = None

    @classmethod
    def inst(cls):
        '''
        For performance reasons, we use singleton to store input
        SampleQuote which is suppose to be the only input in
        this case.
        '''
        if not cls.instance:
            cls.instance = SampleQuote()
            cls.instance.load_def_from_dict(metas)
            cls.instance.set_global_imports(imports)
            cls.instance.granularity = granularity
        return cls.instance

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.open: float = 0.0
        self.close: float = 0.0
        self.high: float = 0.0
        self.low: float = 0.0
        self.volume: int = 0
        self.turnover: float = 0.0
        self.meta_name = 'SampleQuote'
        self.revision = (1 << 32)-1
        self.namespace = pc.namespace_global


class DualMA(pcts3.sv_object):
    '''
    Represents an instance of indicator output defined in uout.json.
    class DualMA extends sv_object which is a wrapper of pycaitlyn.StructValue.
    pycaitlyn.StructValue is a C++ class to manipulate indicator object in lower level.
    '''
    cache = {}

    time_window = (5, 20)

    @classmethod
    def find(cls, market, code):
        key = (market, code)
        cache = cls.cache
        if key not in cache:
            cache[key] = DualMA()
            x = cache[key]
            x.granularity = granularity
            x.market = market
            x.code = code
            x.revision = (1<<32) - 1
            x.load_def_from_dict(metas)
            
        return cache[key]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.meta_name = 'DualMA'
        self.namespace = pc.namespace_private
        self.mal: float = 0.0
        self.mas: float = 0.0
        self.direction: int = -1
        self.prices: list = []
        self.persistent = True

    async def on_sample_quote(self, q: SampleQuote):
        '''
        Calculate DualMA value according to the latest candle stick
        '''
        if self.timetag is None or q.timetag > self.timetag or len(self.prices) == 0:
            self.prices.append(q.close)
        else:
            self.prices[-1] = q.close

        self.timetag = q.timetag

        x, y = DualMA.time_window
        if len(self.prices) > y:
            self.prices = self.prices[-y:]
        X, Y = self.prices[-x:], self.prices[-y:]
        self.mal = np.sum(Y)/len(Y)
        self.mas = np.sum(X)/len(X)
        if np.isclose(self.mal, self.mas):
            self.direction = 0
        else:
            self.direction = -1 if self.mal > self.mas else 1
        return self


async def on_market_open(market, tradeday, time_tag, time_string):
    """
    Market open event
    Parameters:
    tradeday: int
    time_tag: UTC time stamp
    time_string: YYYY-mm-ddTHH:MM::SS+TZ
    """
    pass


async def on_market_close(market, tradeday, timetag, timestring):
    """
    Market close event
    Parameters:
    @tradeday: int
    @time_tag: UTC time stamp
    @time_string: YYYY-mm-ddTHH:MM::SS+TZ
    """
    pass


async def on_tradeday_begin(market, tradeday, time_tag, time_string):
    """
    Tradeday begin event
    Parameters:
    tradeday: int
    time_tag: UTC time stamp
    time_string: YYYY-mm-ddTHH:MM::SS+TZ
    """
    pass


async def on_tradeday_end(market, tradeday, timetag, timestring):
    """
    Tradeday end event
    Parameters:
    @tradeday: int
    @time_tag: UTC time stamp
    @time_string: YYYY-mm-ddTHH:MM::SS+TZ
    """
    pass


async def on_reference(market, tradeday, data, timetag, timestring):
    """
    Refrence data pushed to calculator on each trade day.
    Parameters:
    @data: {
        "holiday": {},
        "stock": {

        },
        "commodity": {

        },
        "futures": {

        },
        "dividend": {

        },
        "security": {

        }
    }
    @tradeday: int
    @time_tag: UTC time stamp
    @time_string: YYYY-mm-ddTHH:MM::SS+TZ
    """
    pass


async def on_init():
    '''
    This event will be fired after metas are received and before on_ready.
    You should fetch historical data and recover the scenario here.
    '''
    pass


async def on_ready():
    '''
    This event will be fired after on_init;
    '''
    pass


async def on_bar(_bar: pc.StructValue):
    """
    _bar is a pc.StuctValue object. All imported data will be fed here.
    As in this case, we are suppose to receive only global::SampleQuote as
    the true input. 
    The output struct values which has the definition and name in uout.json
    will also be fed here for rebuilding indicator historical value purpose.
    Return: this function will return a clone of pc.StructValue object as the 
    output. Or it can also return a list of pc.StructValue objects.
    """
    sample_quote: SampleQuote = SampleQuote.inst()
    ret = []
    if _bar.get_meta_id() == sample_quote.meta_id and \
            _bar.get_namespace() == sample_quote.namespace:
        sample_quote.market = _bar.get_market()
        sample_quote.code = _bar.get_stock_code()
        sample_quote.from_sv(_bar)
        dualma: DualMA = DualMA.find(sample_quote.market, sample_quote.code)
        s = await dualma.on_sample_quote(sample_quote)
        ret.append(s.copy_to_sv())
    return ret


# async def on_reduce(bar):
#     return None
