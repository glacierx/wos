# Getting started

## Tutorial

[![Alt text](https://img.youtube.com/vi/y5BV-Dpx3iM/0.jpg)](https://www.youtube.com/watch?v=y5BV-Dpx3iM)

![alt text](docs/imgs/wos-portal.png)
![alt text](docs/imgs/wos-algo.png)
![alt text](docs/imgs/wos-monitor.png)
![alt text](docs/imgs/wos-charts.png)
![alt text](docs/imgs/wos-trade.png)

## Download Docker Images

Wolverine OS provides two Docker image families:

* **wos-?**: This is a lightweight Docker image that is designed to work with well-maintained service environments. It is typically used for developing indicators and other algorithm-based applications. The image provides a range of tools and utilities for development and testing, including C++ libraries, Python packages, and other dependencies.

* **wos-?-s**: This is a heavier Docker image that provides a standalone environment for developing and testing trading strategies. It includes all the backend web services and C++ infrastructure needed to build a standalone environment without relying on external service environments. The image is designed for more advanced development work, such as extending the C++ services or building Python-C++ modules.

Both Docker images provide a convenient and portable way to work with Wolverine OS. They allow you to quickly set up and configure an environment for developing and testing trading strategies, without having to worry about dependencies or installation issues. Whether you're a quantitative trader, a financial analyst, or a software developer, Wolverine OS Docker images provide a powerful and flexible platform for developing and testing trading strategies in a secure and reliable environment.

`wos-?-s` is an excellent all-in-one starting point that is suitable for individual or medium team users with small to medium data and computing scale requirements. However, it is not yet ready for use in very large-scale practices, such as providing data and computing capabilities to a large community which is the designated function scope of our project. For such use cases, Kubernetes can be used to extend wos-dev-s to a highly scalable state, allowing for the use of many CPUs and GPUs across multiple physical or virtual hosts. With Kubernetes, Wolverine OS can scale to meet the needs of even the most demanding trading strategies and financial quantitative experiments.

### Intel X86_64 architectures

#### Development environment

```
docker pull glacierx/wos-dev
```

```
docker pull glacierx/wos-dev-s
```

#### Production environment

```
docker pull glacierx/wos-dev-prod
```

```
docker pull glacierx/wos-dev-s-prod
```

### Apple Silicon or other aarch64 architechures:

#### Development environment

```
docker pull glacierx/wos-dev-arm64
```

```
docker pull glacierx/wos-dev-s-arm64
```

#### Production environment

```
docker pull glacierx/wos-dev-prod-arm64
```

```
docker pull glacierx/wos-dev-s-prod-arm64
```

## A brief introduction to Wolverine OS

Wolverine OS is a reliable and battle-tested virtual operating system designed for financial quantitative experiments, manual and automated trading, and risk management. It is built as a docker container-based system, making it easy to deploy and use on a variety of platforms.

Wolverine OS includes a range of features for developing and executing trading strategies, including simulated trading accounts with real-time market data, indicator-based development and backtesting, and debugging and monitoring tools. The system also includes risk management and compliance functions, ensuring that trading activities comply with regulatory requirements.

Wolverine OS is based on a scalable design and has been developed over the years to include a wide range of C++-based services and an API-based management web site backend. The system has been used to execute live trade signals in different markets around the world for a long time, demonstrating its reliability and stability in production environments.

Whether you're a quantitative trader, a financial analyst, or a software developer, Wolverine OS provides a powerful and flexible platform for developing and testing trading strategies in a secure and reliable environment.


Wolverine OS consists of two main executable branches:

* **Dev**: This branch should be used with the dev service environment, unless you are using the wos-dev-s Docker container to build a standalone environment without a global data repository. Please note that the dev branch is only compatible with the dev service environment. If you try to send requests from a wos-dev container to wos-dev-s-prod services, undefined behavior may occur.

* **Prod**: This branch should be used with the production service environment. Please note that the dev branch is not compatible with the prod branch.

The Wolverine OS system is designed to have two main parts:

* **Global**: This is a read-only data repository that provides global market real-time and historical multi-timeframe sampled data. Global environment is maintained by us. If you want to build your own private environment from scratch, the best practice is to work with the global environment. However, please note that we do not publicly give access to our global service. If you are interested, please contact us.

* **Private**: This is a writable data repository that users can use to perform experiments and trading practices. A system without access to the global repository can exist without any issues. If you don't want to use out-of-the-box data and services  which will involve global environment to perform experiments, you can run a standalone private-only system and use indicator-based solutions or our open API to develop an advanced data pumping service, such as dirac-client, to import raw data. You can then use the algorithm development module to process and generate more indicators as needed.

By separating the global and private repositories, Wolverine OS provides a flexible and secure environment for developing and testing trading strategies. The dev and prod branches also provide different levels of compatibility with service environments, allowing you to choose the appropriate branch for your needs.

### Chart

The chart module in Wolverine OS provides a rich and interactive visual environment for developing and testing trading strategies. The chart module is designed to be easy to use, with a range of both dedicated algorithm models in python and simple one-ticker indicator in formula language (we call it Feynman language after the great Nobel prize winner) for drawing fancy charts and indicator widgets.

If you are familiar with Chinese financial software, you will appreciate the ability to import simple one-ticker indicator source code and seamlessly see the results in the chart module. The module also supports multi-timeframe sampled data, allowing for detailed analysis and candlestick-based strategies.

In addition to its powerful visualization capabilities, the chart module also includes an embedded order entry module, allowing for seamless trade execution and monitoring. User doodles can also be created using the indicator language, providing a flexible and customizable environment for experimentation and analysis.

Whether you're a quantitative trader, a financial analyst, or a software developer, Wolverine OS chart module provides a powerful and flexible platform for developing and testing trading strategies in a secure and reliable environment. With its rich and interactive graphics and advanced analysis tools, the chart module is the perfect tool for exploring market trends and developing new trading strategies.

### Formula

#### Feynman Language

Feynman language is based on a popular single-ticker indicator language that can be found in Wind (万得), Straight Flush (同花顺), and many similar competitors. However, Feynman language offers more features than the original version of the indicator language, including:

* **User-defined functions**: users can define their own functions and incorporate them with their dedicate designed python algorithm models.

* **Global cross-references**: Feynman language allows for cross-referencing data from both the user-authored indicators or those indicators user authorized to access. Fields of those indicators can be referenced in one piece of formula easily.

* **Doodles**: users can create custom graphical elements and annotations to enhance their analysis and visualization of market data.

* **Seamless data interface**: Feynman language provides a seamless interface between global and private dual environments, making it easy to access and analyze data from multiple sources.


Overall, Feynman language provides a powerful and flexible platform for developing and testing trading strategies in Wolverine OS. Whether you're a quantitative trader, a financial analyst, or a software developer, Feynman language offers a range of features and capabilities that make it easy to build sophisticated trading strategies and algorithms.

BOLL

```
variable : N= 15, P= 3, BBI=0;
BBI:=(MA(CLOSE,3)+MA(CLOSE,6)+MA(CLOSE,12)+MA(CLOSE,24))/4;
DWN:(BBI-P*STD(BBI,N)),LINETHICK1, COLORFF0000;
UPR:(BBI+P*STD(BBI,N)),LINETHICK1, COLORFFA13B;
MID: BBI, LINETHICK1, COLOR7E7AFF;
```

More dedicated example used with python algorithm and cross referencing.

```
xref: w = "{market}/{code}/TQF1210_1H_L3/wp";
line(time_tag[1],80,time_tag,80,"COLOR:00BCD4,LINETHICK:1,STYLE:solid");
line(time_tag[1],-80,time_tag,-80,"COLOR:00BCD4,LINETHICK:1,STYLE:solid");
wp: w, LINETHICK:2, COLOR:FF9800,STYLE:line;
```

Here `w` is a cross reference to a field `wp` of a python model named `TQF1210_1H_L3` developed by our user.

### Model Development

Wolverine OS is designed for dedicated quantitative model development and experimentation. It provides a powerful platform for developing quantitative models ranging from simple dual moving average trend following strategies to deep neural network-based models.

For integrated graphical development environments, VSCode is a popular choice. Users can use VSCode in native or remote mode to develop, debug, and monitor their models. Wolverine OS also supports a range of other development environments and tools, making it easy to work with the platform in a way that best suits your needs and preferences.


#### Backtest

Backtesting is a critical process for quantitative model development and experimentation. Wolverine OS provides a flexible and powerful backtesting subsystem that supports multiple development languages, including Python3, which is the language we highly recommend.

The core and resource-intensive parts of the backtesting subsystem are developed using high-performance C++ language, with a variety of language bindings provided. Both single CPU core mode and multiple CPU core mode are supported, and in the latter case, a cluster of physical hosts or GPUs can be used to accelerate the process significantly.

Users can choose to use an IDE within the application or VSCode for backtesting, and auto code completion and model templates are available to streamline the process. With Wolverine OS, you can easily develop and test sophisticated quantitative models and trading strategies, giving you the tools you need to succeed in today's dynamic financial markets.

#### Indictator

Sophisticated quantitative models are often built on a forest of single indicators, which may be developed using raw external market data or a multi-tier pipeline referencing each other in a complex manner.

Wolverine OS provides an indicator backtesting system that allows you to develop single low-level indicators that don't reference any other indicators but only use external data or referencing the live indicators arbitrarily when you are properly authorized. Each backtesting instance is separate, so users can compare multiple backtesting generations of the same model. Different revisions of the output indicator value will also be saved.

The indicator output can be visualized in the chart module, or more widely adopted by our users, it can be used seamlessly with Feynman language. Wrapped by Feynman language, all the interactive functions of the language engine can be used with no extra effort.

After a series of iterative backtests, users can let an indicator go live, which can be used to solve very challenging real-time problems like HFT. Wolverine OS provides a flexible and powerful platform for developing, testing, and deploying sophisticated indicators, giving you the tools you need to succeed in today's dynamic financial markets.


#### Strategy

A strategy is another form of quantitative model that is more focused on signal execution. Compared to indicators, strategies are more focused on how to execute a set of high-quality trading signals.

Signal execution is a very different domain from numeric computing-based development, which is heavily used in indicator development. Signal execution is more real-time, and as it becomes more low-latency, quantum effects become increasingly significant. Meanwhile, account execution involves different money capacity levels ranging from single-lot trading accounts to large-scale production accounts used by institutional trading firms. Dividing a big trading account into smaller sub-accounts and mapping each sub-account to follow different quantitative signals can make the situation complex beyond most users' imaginations.

To solve these problems, a wide range of techniques are involved, such as slippage simulation, error correction mechanisms, and order book prediction.

Using the strategy backtesting function together with indicator backtesting, users can thoroughly test their strategy theoretically and almost practically. Multi-physical account and multi-basket account level backtesting can be well-supported in this subsystem. Wolverine OS provides a flexible and powerful platform for developing, testing, and deploying sophisticated trading strategies, giving you the tools you need to succeed in today's dynamic financial markets.

### Account Management

Wolverine OS is designed to support managing multiple trading accounts from different clearing brokers around the world. In China Mainland commodity and financial future and option markets, all brokers that have adopted CTP as their trading backend will be supported with no issues.

Both human traders and quantitative live models can generate signals in the system. Any physical trading account can be divided into smaller sub-accounts, each of which can be assigned to different Wolverine OS system users to allow them to manually enter orders or follow model-generated signals automatically.

As any single quantitative model can maintain a series of baskets, which are typically used to trade basis arbitrage strategies that trade a set of securities and use specific future contracts as a hedge, the relationship between sub-accounts and signals is multiple to multiple. Traders can operate multiple sub-accounts to build their portfolios.

### Simulated trading

As Wolverine OS initially targets small trading teams and individual traders, simulated trading functions are a very important feature to give them a very real sandbox for training and testing purposes.

Technologies invented in the strategy backtesting were widely adopted in the Simulated Trading module. We have defined many parameters to illustrate the properties of a trading account's performance in the live market in which quantum effects appear to be the norm.

We provide a default set of configurations that adequately fit the average environment feature in different markets. These configurations include slippage ratio, order to transaction latency, measurement uncertainty of the order book liquidity, and more. Currently the default configurations are backed by machine learning technique. User can manually change configuration to create more crucial environment or use their more sophisticated model to give more accurate configuration for their specific purposes.

The typical use case for the simulated trading feature is to train a newbie manual trader or to test the about-to-go-live quantitative strategies.

Simulated trading has been used as an efficient approach to let traders learn the techniques to survive, even those who have no background in trading. Compared to traditional trading firms' way of training traders, this innovative approach shows very compelling attractiveness in terms of economic and performance aspects.

As a measure to guarantee that the strategies will adopt the market as expected, which is the opposite of overfitting, the simulated trading function has helped our users save a lot of money that would have been wasted in the market due to overfitting and researchers' hallucination on the performance.


### Mark To Market

Positions are generated by manual traders or quantitative models in Wolverine OS by executing signals. Sub-accounts and physical accounts are used to contain positions and trades.

However, there are more complex cases where traders will build multi-purpose trading books or portfolios by organizing different sub-accounts. Money and positions can flow between sub-accounts in real-time.

Therefore, calculating exposure and profit in different dimensions becomes a critical and challenging task. The Mark To Market module, as a very essential built-in mechanism of risk management, is introduced in Wolverine OS.

Using the MtM module, all of the portfolio's risk metrics can be calculated as the markets are ticking in a very low latency and accurate manner. Typically, the net value of any portfolios, sub-accounts, physical accounts, traders can be computed accurately. This important feature is missing in most trading systems in the market, making it a challenging problem to calculate the margin used by different position containers. Therefore, initial investment on each portfolio, trader, sub-account can be very hard to track without proper tools.

The Mark To Market module provides a reliable and efficient tool for tracking the performance of trading portfolios, enabling traders to make informed decisions in real-time. With this module, traders can calculate the net asset value of their portfolios, monitor their exposure, and analyze their performance in a comprehensive and accurate way.

## Examples




## Support