# Getting started

Wolverine OS consists of two main executable branches:

* **Dev**: This branch should be used with the dev service environment, unless you are using the wos-dev-s Docker container to build a standalone environment without a global data repository. Please note that the dev branch is only compatible with the dev service environment. If you try to send requests from a wos-dev container to wos-dev-s-prod services, undefined behavior may occur.

* **Prod**: This branch should be used with the production service environment. Please note that the dev branch is not compatible with the prod branch.

The Wolverine OS system is designed to have two main parts:

* **Global**: This is a read-only data repository that provides global market real-time and historical multi-timeframe sampled data. If you want to build your own private environment from scratch, the best practice is to work with the global environment. However, please note that we do not publicly give access to our global service. If you are interested, please contact us.

* **Private**: This is a writable data repository that users can use to perform experiments and trading practices. A system without access to the global repository can exist without any issues. If you want to use out-of-the-box data and services to perform experiments, you can run a standalone private-only system and use indicator-based solutions or our open API to develop an advanced data pumping service, such as dirac-client, to import raw data. You can then use the algorithm development module to process and generate more indicators as needed.

By separating the global and private repositories, Wolverine OS provides a flexible and secure environment for developing and testing trading strategies. The dev and prod branches also provide different levels of compatibility with service environments, allowing you to choose the appropriate branch for your needs.

## Download Docker Images

### Intel X86_64 architectures:

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

### Apple M1 architechures:

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

### Chart

### Formula

#### Feynman Language

### Model Development

#### Backtest

#### Indictator

#### Strategy

### Mark To Market

### Account Management

## Examples

This repository is to demonstrate the basic usage of `glacierx/wos-dev` image and `glacierx/wos-dev-s` image. They are designed to provide indicator based development, debugging, monitoring functions and a all-in-one standalone server and client envirionment for testing and devlopment purpose respectively.

You can find many templates of indicators development on Wolverine OS. 

## Support