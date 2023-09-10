from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetInfoRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetInfoResponse(_message.Message):
    __slots__ = ["uptime", "available_exchanges", "enabled_exchanges", "default_forex_provider", "default_fiat_currency", "subsystem_status", "rpc_endpoints"]
    class SubsystemStatusEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    class RpcEndpointsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: RPCEndpoint
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[RPCEndpoint, _Mapping]] = ...) -> None: ...
    UPTIME_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_EXCHANGES_FIELD_NUMBER: _ClassVar[int]
    ENABLED_EXCHANGES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FOREX_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIAT_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    SUBSYSTEM_STATUS_FIELD_NUMBER: _ClassVar[int]
    RPC_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    uptime: str
    available_exchanges: int
    enabled_exchanges: int
    default_forex_provider: str
    default_fiat_currency: str
    subsystem_status: _containers.ScalarMap[str, bool]
    rpc_endpoints: _containers.MessageMap[str, RPCEndpoint]
    def __init__(self, uptime: _Optional[str] = ..., available_exchanges: _Optional[int] = ..., enabled_exchanges: _Optional[int] = ..., default_forex_provider: _Optional[str] = ..., default_fiat_currency: _Optional[str] = ..., subsystem_status: _Optional[_Mapping[str, bool]] = ..., rpc_endpoints: _Optional[_Mapping[str, RPCEndpoint]] = ...) -> None: ...

class GetCommunicationRelayersRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CommunicationRelayer(_message.Message):
    __slots__ = ["enabled", "connected"]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    connected: bool
    def __init__(self, enabled: bool = ..., connected: bool = ...) -> None: ...

class GetCommunicationRelayersResponse(_message.Message):
    __slots__ = ["communication_relayers"]
    class CommunicationRelayersEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CommunicationRelayer
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CommunicationRelayer, _Mapping]] = ...) -> None: ...
    COMMUNICATION_RELAYERS_FIELD_NUMBER: _ClassVar[int]
    communication_relayers: _containers.MessageMap[str, CommunicationRelayer]
    def __init__(self, communication_relayers: _Optional[_Mapping[str, CommunicationRelayer]] = ...) -> None: ...

class GenericSubsystemRequest(_message.Message):
    __slots__ = ["subsystem"]
    SUBSYSTEM_FIELD_NUMBER: _ClassVar[int]
    subsystem: str
    def __init__(self, subsystem: _Optional[str] = ...) -> None: ...

class GetSubsystemsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetSusbsytemsResponse(_message.Message):
    __slots__ = ["subsystems_status"]
    class SubsystemsStatusEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    SUBSYSTEMS_STATUS_FIELD_NUMBER: _ClassVar[int]
    subsystems_status: _containers.ScalarMap[str, bool]
    def __init__(self, subsystems_status: _Optional[_Mapping[str, bool]] = ...) -> None: ...

class GetRPCEndpointsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RPCEndpoint(_message.Message):
    __slots__ = ["started", "listen_address"]
    STARTED_FIELD_NUMBER: _ClassVar[int]
    LISTEN_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    started: bool
    listen_address: str
    def __init__(self, started: bool = ..., listen_address: _Optional[str] = ...) -> None: ...

class GetRPCEndpointsResponse(_message.Message):
    __slots__ = ["endpoints"]
    class EndpointsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: RPCEndpoint
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[RPCEndpoint, _Mapping]] = ...) -> None: ...
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    endpoints: _containers.MessageMap[str, RPCEndpoint]
    def __init__(self, endpoints: _Optional[_Mapping[str, RPCEndpoint]] = ...) -> None: ...

class GenericExchangeNameRequest(_message.Message):
    __slots__ = ["exchange"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    def __init__(self, exchange: _Optional[str] = ...) -> None: ...

class GetExchangesRequest(_message.Message):
    __slots__ = ["enabled"]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class GetExchangesResponse(_message.Message):
    __slots__ = ["exchanges"]
    EXCHANGES_FIELD_NUMBER: _ClassVar[int]
    exchanges: str
    def __init__(self, exchanges: _Optional[str] = ...) -> None: ...

class GetExchangeOTPResponse(_message.Message):
    __slots__ = ["otp_code"]
    OTP_CODE_FIELD_NUMBER: _ClassVar[int]
    otp_code: str
    def __init__(self, otp_code: _Optional[str] = ...) -> None: ...

class GetExchangeOTPsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetExchangeOTPsResponse(_message.Message):
    __slots__ = ["otp_codes"]
    class OtpCodesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    OTP_CODES_FIELD_NUMBER: _ClassVar[int]
    otp_codes: _containers.ScalarMap[str, str]
    def __init__(self, otp_codes: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DisableExchangeRequest(_message.Message):
    __slots__ = ["exchange"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    def __init__(self, exchange: _Optional[str] = ...) -> None: ...

class PairsSupported(_message.Message):
    __slots__ = ["available_pairs", "enabled_pairs"]
    AVAILABLE_PAIRS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_PAIRS_FIELD_NUMBER: _ClassVar[int]
    available_pairs: str
    enabled_pairs: str
    def __init__(self, available_pairs: _Optional[str] = ..., enabled_pairs: _Optional[str] = ...) -> None: ...

class GetExchangeInfoResponse(_message.Message):
    __slots__ = ["name", "enabled", "verbose", "using_sandbox", "http_timeout", "http_useragent", "http_proxy", "base_currencies", "supported_assets", "authenticated_api"]
    class SupportedAssetsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: PairsSupported
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[PairsSupported, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    USING_SANDBOX_FIELD_NUMBER: _ClassVar[int]
    HTTP_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    HTTP_USERAGENT_FIELD_NUMBER: _ClassVar[int]
    HTTP_PROXY_FIELD_NUMBER: _ClassVar[int]
    BASE_CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_ASSETS_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATED_API_FIELD_NUMBER: _ClassVar[int]
    name: str
    enabled: bool
    verbose: bool
    using_sandbox: bool
    http_timeout: str
    http_useragent: str
    http_proxy: str
    base_currencies: str
    supported_assets: _containers.MessageMap[str, PairsSupported]
    authenticated_api: bool
    def __init__(self, name: _Optional[str] = ..., enabled: bool = ..., verbose: bool = ..., using_sandbox: bool = ..., http_timeout: _Optional[str] = ..., http_useragent: _Optional[str] = ..., http_proxy: _Optional[str] = ..., base_currencies: _Optional[str] = ..., supported_assets: _Optional[_Mapping[str, PairsSupported]] = ..., authenticated_api: bool = ...) -> None: ...

class GetTickerRequest(_message.Message):
    __slots__ = ["exchange", "pair", "asset_type"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    pair: CurrencyPair
    asset_type: str
    def __init__(self, exchange: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., asset_type: _Optional[str] = ...) -> None: ...

class CurrencyPair(_message.Message):
    __slots__ = ["delimiter", "base", "quote"]
    DELIMITER_FIELD_NUMBER: _ClassVar[int]
    BASE_FIELD_NUMBER: _ClassVar[int]
    QUOTE_FIELD_NUMBER: _ClassVar[int]
    delimiter: str
    base: str
    quote: str
    def __init__(self, delimiter: _Optional[str] = ..., base: _Optional[str] = ..., quote: _Optional[str] = ...) -> None: ...

class TickerResponse(_message.Message):
    __slots__ = ["pair", "last_updated", "currency_pair", "last", "high", "low", "bid", "ask", "volume", "price_ath"]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_PAIR_FIELD_NUMBER: _ClassVar[int]
    LAST_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    BID_FIELD_NUMBER: _ClassVar[int]
    ASK_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    PRICE_ATH_FIELD_NUMBER: _ClassVar[int]
    pair: CurrencyPair
    last_updated: int
    currency_pair: str
    last: float
    high: float
    low: float
    bid: float
    ask: float
    volume: float
    price_ath: float
    def __init__(self, pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., last_updated: _Optional[int] = ..., currency_pair: _Optional[str] = ..., last: _Optional[float] = ..., high: _Optional[float] = ..., low: _Optional[float] = ..., bid: _Optional[float] = ..., ask: _Optional[float] = ..., volume: _Optional[float] = ..., price_ath: _Optional[float] = ...) -> None: ...

class GetTickersRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Tickers(_message.Message):
    __slots__ = ["exchange", "tickers"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    TICKERS_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    tickers: _containers.RepeatedCompositeFieldContainer[TickerResponse]
    def __init__(self, exchange: _Optional[str] = ..., tickers: _Optional[_Iterable[_Union[TickerResponse, _Mapping]]] = ...) -> None: ...

class GetTickersResponse(_message.Message):
    __slots__ = ["tickers"]
    TICKERS_FIELD_NUMBER: _ClassVar[int]
    tickers: _containers.RepeatedCompositeFieldContainer[Tickers]
    def __init__(self, tickers: _Optional[_Iterable[_Union[Tickers, _Mapping]]] = ...) -> None: ...

class GetOrderbookRequest(_message.Message):
    __slots__ = ["exchange", "pair", "asset_type"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    pair: CurrencyPair
    asset_type: str
    def __init__(self, exchange: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., asset_type: _Optional[str] = ...) -> None: ...

class OrderbookItem(_message.Message):
    __slots__ = ["amount", "price", "id"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    amount: float
    price: float
    id: int
    def __init__(self, amount: _Optional[float] = ..., price: _Optional[float] = ..., id: _Optional[int] = ...) -> None: ...

class OrderbookResponse(_message.Message):
    __slots__ = ["pair", "currency_pair", "bids", "asks", "last_updated", "asset_type", "error"]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_PAIR_FIELD_NUMBER: _ClassVar[int]
    BIDS_FIELD_NUMBER: _ClassVar[int]
    ASKS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    pair: CurrencyPair
    currency_pair: str
    bids: _containers.RepeatedCompositeFieldContainer[OrderbookItem]
    asks: _containers.RepeatedCompositeFieldContainer[OrderbookItem]
    last_updated: int
    asset_type: str
    error: str
    def __init__(self, pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., currency_pair: _Optional[str] = ..., bids: _Optional[_Iterable[_Union[OrderbookItem, _Mapping]]] = ..., asks: _Optional[_Iterable[_Union[OrderbookItem, _Mapping]]] = ..., last_updated: _Optional[int] = ..., asset_type: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class GetOrderbooksRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Orderbooks(_message.Message):
    __slots__ = ["exchange", "orderbooks"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ORDERBOOKS_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    orderbooks: _containers.RepeatedCompositeFieldContainer[OrderbookResponse]
    def __init__(self, exchange: _Optional[str] = ..., orderbooks: _Optional[_Iterable[_Union[OrderbookResponse, _Mapping]]] = ...) -> None: ...

class GetOrderbooksResponse(_message.Message):
    __slots__ = ["orderbooks"]
    ORDERBOOKS_FIELD_NUMBER: _ClassVar[int]
    orderbooks: _containers.RepeatedCompositeFieldContainer[Orderbooks]
    def __init__(self, orderbooks: _Optional[_Iterable[_Union[Orderbooks, _Mapping]]] = ...) -> None: ...

class GetAccountInfoRequest(_message.Message):
    __slots__ = ["exchange", "asset_type"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    asset_type: str
    def __init__(self, exchange: _Optional[str] = ..., asset_type: _Optional[str] = ...) -> None: ...

class Account(_message.Message):
    __slots__ = ["id", "currencies"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    currencies: _containers.RepeatedCompositeFieldContainer[AccountCurrencyInfo]
    def __init__(self, id: _Optional[str] = ..., currencies: _Optional[_Iterable[_Union[AccountCurrencyInfo, _Mapping]]] = ...) -> None: ...

class AccountCurrencyInfo(_message.Message):
    __slots__ = ["currency", "total_value", "hold", "free", "free_without_borrow", "borrowed"]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    HOLD_FIELD_NUMBER: _ClassVar[int]
    FREE_FIELD_NUMBER: _ClassVar[int]
    FREE_WITHOUT_BORROW_FIELD_NUMBER: _ClassVar[int]
    BORROWED_FIELD_NUMBER: _ClassVar[int]
    currency: str
    total_value: float
    hold: float
    free: float
    free_without_borrow: float
    borrowed: float
    def __init__(self, currency: _Optional[str] = ..., total_value: _Optional[float] = ..., hold: _Optional[float] = ..., free: _Optional[float] = ..., free_without_borrow: _Optional[float] = ..., borrowed: _Optional[float] = ...) -> None: ...

class GetAccountInfoResponse(_message.Message):
    __slots__ = ["exchange", "accounts"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    accounts: _containers.RepeatedCompositeFieldContainer[Account]
    def __init__(self, exchange: _Optional[str] = ..., accounts: _Optional[_Iterable[_Union[Account, _Mapping]]] = ...) -> None: ...

class GetConfigRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetConfigResponse(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class PortfolioAddress(_message.Message):
    __slots__ = ["address", "coin_type", "description", "balance"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    COIN_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    address: str
    coin_type: str
    description: str
    balance: float
    def __init__(self, address: _Optional[str] = ..., coin_type: _Optional[str] = ..., description: _Optional[str] = ..., balance: _Optional[float] = ...) -> None: ...

class GetPortfolioRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetPortfolioResponse(_message.Message):
    __slots__ = ["portfolio"]
    PORTFOLIO_FIELD_NUMBER: _ClassVar[int]
    portfolio: _containers.RepeatedCompositeFieldContainer[PortfolioAddress]
    def __init__(self, portfolio: _Optional[_Iterable[_Union[PortfolioAddress, _Mapping]]] = ...) -> None: ...

class GetPortfolioSummaryRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Coin(_message.Message):
    __slots__ = ["coin", "balance", "address", "percentage"]
    COIN_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    coin: str
    balance: float
    address: str
    percentage: float
    def __init__(self, coin: _Optional[str] = ..., balance: _Optional[float] = ..., address: _Optional[str] = ..., percentage: _Optional[float] = ...) -> None: ...

class OfflineCoinSummary(_message.Message):
    __slots__ = ["address", "balance", "percentage"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    address: str
    balance: float
    percentage: float
    def __init__(self, address: _Optional[str] = ..., balance: _Optional[float] = ..., percentage: _Optional[float] = ...) -> None: ...

class OnlineCoinSummary(_message.Message):
    __slots__ = ["balance", "percentage"]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    balance: float
    percentage: float
    def __init__(self, balance: _Optional[float] = ..., percentage: _Optional[float] = ...) -> None: ...

class OfflineCoins(_message.Message):
    __slots__ = ["addresses"]
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    addresses: _containers.RepeatedCompositeFieldContainer[OfflineCoinSummary]
    def __init__(self, addresses: _Optional[_Iterable[_Union[OfflineCoinSummary, _Mapping]]] = ...) -> None: ...

class OnlineCoins(_message.Message):
    __slots__ = ["coins"]
    class CoinsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: OnlineCoinSummary
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[OnlineCoinSummary, _Mapping]] = ...) -> None: ...
    COINS_FIELD_NUMBER: _ClassVar[int]
    coins: _containers.MessageMap[str, OnlineCoinSummary]
    def __init__(self, coins: _Optional[_Mapping[str, OnlineCoinSummary]] = ...) -> None: ...

class GetPortfolioSummaryResponse(_message.Message):
    __slots__ = ["coin_totals", "coins_offline", "coins_offline_summary", "coins_online", "coins_online_summary"]
    class CoinsOfflineSummaryEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: OfflineCoins
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[OfflineCoins, _Mapping]] = ...) -> None: ...
    class CoinsOnlineSummaryEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: OnlineCoins
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[OnlineCoins, _Mapping]] = ...) -> None: ...
    COIN_TOTALS_FIELD_NUMBER: _ClassVar[int]
    COINS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
    COINS_OFFLINE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    COINS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    COINS_ONLINE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    coin_totals: _containers.RepeatedCompositeFieldContainer[Coin]
    coins_offline: _containers.RepeatedCompositeFieldContainer[Coin]
    coins_offline_summary: _containers.MessageMap[str, OfflineCoins]
    coins_online: _containers.RepeatedCompositeFieldContainer[Coin]
    coins_online_summary: _containers.MessageMap[str, OnlineCoins]
    def __init__(self, coin_totals: _Optional[_Iterable[_Union[Coin, _Mapping]]] = ..., coins_offline: _Optional[_Iterable[_Union[Coin, _Mapping]]] = ..., coins_offline_summary: _Optional[_Mapping[str, OfflineCoins]] = ..., coins_online: _Optional[_Iterable[_Union[Coin, _Mapping]]] = ..., coins_online_summary: _Optional[_Mapping[str, OnlineCoins]] = ...) -> None: ...

class AddPortfolioAddressRequest(_message.Message):
    __slots__ = ["address", "coin_type", "description", "balance", "supported_exchanges", "cold_storage"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    COIN_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_EXCHANGES_FIELD_NUMBER: _ClassVar[int]
    COLD_STORAGE_FIELD_NUMBER: _ClassVar[int]
    address: str
    coin_type: str
    description: str
    balance: float
    supported_exchanges: str
    cold_storage: bool
    def __init__(self, address: _Optional[str] = ..., coin_type: _Optional[str] = ..., description: _Optional[str] = ..., balance: _Optional[float] = ..., supported_exchanges: _Optional[str] = ..., cold_storage: bool = ...) -> None: ...

class RemovePortfolioAddressRequest(_message.Message):
    __slots__ = ["address", "coin_type", "description"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    COIN_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    address: str
    coin_type: str
    description: str
    def __init__(self, address: _Optional[str] = ..., coin_type: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class GetForexProvidersRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ForexProvider(_message.Message):
    __slots__ = ["name", "enabled", "verbose", "rest_polling_delay", "api_key", "api_key_level", "primary_provider"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    REST_POLLING_DELAY_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    API_KEY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    name: str
    enabled: bool
    verbose: bool
    rest_polling_delay: str
    api_key: str
    api_key_level: int
    primary_provider: bool
    def __init__(self, name: _Optional[str] = ..., enabled: bool = ..., verbose: bool = ..., rest_polling_delay: _Optional[str] = ..., api_key: _Optional[str] = ..., api_key_level: _Optional[int] = ..., primary_provider: bool = ...) -> None: ...

class GetForexProvidersResponse(_message.Message):
    __slots__ = ["forex_providers"]
    FOREX_PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    forex_providers: _containers.RepeatedCompositeFieldContainer[ForexProvider]
    def __init__(self, forex_providers: _Optional[_Iterable[_Union[ForexProvider, _Mapping]]] = ...) -> None: ...

class GetForexRatesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ForexRatesConversion(_message.Message):
    __slots__ = ["to", "rate", "inverse_rate"]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    INVERSE_RATE_FIELD_NUMBER: _ClassVar[int]
    to: str
    rate: float
    inverse_rate: float
    def __init__(self, to: _Optional[str] = ..., rate: _Optional[float] = ..., inverse_rate: _Optional[float] = ..., **kwargs) -> None: ...

class GetForexRatesResponse(_message.Message):
    __slots__ = ["forex_rates"]
    FOREX_RATES_FIELD_NUMBER: _ClassVar[int]
    forex_rates: _containers.RepeatedCompositeFieldContainer[ForexRatesConversion]
    def __init__(self, forex_rates: _Optional[_Iterable[_Union[ForexRatesConversion, _Mapping]]] = ...) -> None: ...

class OrderDetails(_message.Message):
    __slots__ = ["exchange", "id", "client_order_id", "base_currency", "quote_currency", "asset_type", "order_side", "order_type", "creation_time", "update_time", "status", "price", "amount", "open_volume", "fee", "cost", "trades"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    QUOTE_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    ORDER_SIDE_FIELD_NUMBER: _ClassVar[int]
    ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    OPEN_VOLUME_FIELD_NUMBER: _ClassVar[int]
    FEE_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    TRADES_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    id: str
    client_order_id: str
    base_currency: str
    quote_currency: str
    asset_type: str
    order_side: str
    order_type: str
    creation_time: str
    update_time: str
    status: str
    price: float
    amount: float
    open_volume: float
    fee: float
    cost: float
    trades: _containers.RepeatedCompositeFieldContainer[TradeHistory]
    def __init__(self, exchange: _Optional[str] = ..., id: _Optional[str] = ..., client_order_id: _Optional[str] = ..., base_currency: _Optional[str] = ..., quote_currency: _Optional[str] = ..., asset_type: _Optional[str] = ..., order_side: _Optional[str] = ..., order_type: _Optional[str] = ..., creation_time: _Optional[str] = ..., update_time: _Optional[str] = ..., status: _Optional[str] = ..., price: _Optional[float] = ..., amount: _Optional[float] = ..., open_volume: _Optional[float] = ..., fee: _Optional[float] = ..., cost: _Optional[float] = ..., trades: _Optional[_Iterable[_Union[TradeHistory, _Mapping]]] = ...) -> None: ...

class TradeHistory(_message.Message):
    __slots__ = ["creation_time", "id", "price", "amount", "exchange", "asset_type", "order_side", "fee", "total"]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    ORDER_SIDE_FIELD_NUMBER: _ClassVar[int]
    FEE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    creation_time: int
    id: str
    price: float
    amount: float
    exchange: str
    asset_type: str
    order_side: str
    fee: float
    total: float
    def __init__(self, creation_time: _Optional[int] = ..., id: _Optional[str] = ..., price: _Optional[float] = ..., amount: _Optional[float] = ..., exchange: _Optional[str] = ..., asset_type: _Optional[str] = ..., order_side: _Optional[str] = ..., fee: _Optional[float] = ..., total: _Optional[float] = ...) -> None: ...

class GetOrdersRequest(_message.Message):
    __slots__ = ["exchange", "asset_type", "pair", "start_date", "end_date"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    asset_type: str
    pair: CurrencyPair
    start_date: str
    end_date: str
    def __init__(self, exchange: _Optional[str] = ..., asset_type: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., start_date: _Optional[str] = ..., end_date: _Optional[str] = ...) -> None: ...

class GetOrdersResponse(_message.Message):
    __slots__ = ["orders"]
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    orders: _containers.RepeatedCompositeFieldContainer[OrderDetails]
    def __init__(self, orders: _Optional[_Iterable[_Union[OrderDetails, _Mapping]]] = ...) -> None: ...

class GetOrderRequest(_message.Message):
    __slots__ = ["exchange", "order_id", "pair", "asset"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    order_id: str
    pair: CurrencyPair
    asset: str
    def __init__(self, exchange: _Optional[str] = ..., order_id: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., asset: _Optional[str] = ...) -> None: ...

class SubmitOrderRequest(_message.Message):
    __slots__ = ["exchange", "pair", "side", "order_type", "amount", "price", "client_id", "asset_type"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    pair: CurrencyPair
    side: str
    order_type: str
    amount: float
    price: float
    client_id: str
    asset_type: str
    def __init__(self, exchange: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., side: _Optional[str] = ..., order_type: _Optional[str] = ..., amount: _Optional[float] = ..., price: _Optional[float] = ..., client_id: _Optional[str] = ..., asset_type: _Optional[str] = ...) -> None: ...

class Trades(_message.Message):
    __slots__ = ["amount", "price", "fee", "fee_asset"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    FEE_FIELD_NUMBER: _ClassVar[int]
    FEE_ASSET_FIELD_NUMBER: _ClassVar[int]
    amount: float
    price: float
    fee: float
    fee_asset: str
    def __init__(self, amount: _Optional[float] = ..., price: _Optional[float] = ..., fee: _Optional[float] = ..., fee_asset: _Optional[str] = ...) -> None: ...

class SubmitOrderResponse(_message.Message):
    __slots__ = ["order_placed", "order_id", "trades"]
    ORDER_PLACED_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    TRADES_FIELD_NUMBER: _ClassVar[int]
    order_placed: bool
    order_id: str
    trades: _containers.RepeatedCompositeFieldContainer[Trades]
    def __init__(self, order_placed: bool = ..., order_id: _Optional[str] = ..., trades: _Optional[_Iterable[_Union[Trades, _Mapping]]] = ...) -> None: ...

class SimulateOrderRequest(_message.Message):
    __slots__ = ["exchange", "pair", "amount", "side"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    pair: CurrencyPair
    amount: float
    side: str
    def __init__(self, exchange: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., amount: _Optional[float] = ..., side: _Optional[str] = ...) -> None: ...

class SimulateOrderResponse(_message.Message):
    __slots__ = ["orders", "amount", "minimum_price", "maximum_price", "percentage_gain_loss", "status"]
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_PRICE_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_PRICE_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_GAIN_LOSS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    orders: _containers.RepeatedCompositeFieldContainer[OrderbookItem]
    amount: float
    minimum_price: float
    maximum_price: float
    percentage_gain_loss: float
    status: str
    def __init__(self, orders: _Optional[_Iterable[_Union[OrderbookItem, _Mapping]]] = ..., amount: _Optional[float] = ..., minimum_price: _Optional[float] = ..., maximum_price: _Optional[float] = ..., percentage_gain_loss: _Optional[float] = ..., status: _Optional[str] = ...) -> None: ...

class WhaleBombRequest(_message.Message):
    __slots__ = ["exchange", "pair", "price_target", "side", "asset_type"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    PRICE_TARGET_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    pair: CurrencyPair
    price_target: float
    side: str
    asset_type: str
    def __init__(self, exchange: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., price_target: _Optional[float] = ..., side: _Optional[str] = ..., asset_type: _Optional[str] = ...) -> None: ...

class CancelOrderRequest(_message.Message):
    __slots__ = ["exchange", "account_id", "order_id", "pair", "asset_type", "wallet_address", "side"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    WALLET_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    account_id: str
    order_id: str
    pair: CurrencyPair
    asset_type: str
    wallet_address: str
    side: str
    def __init__(self, exchange: _Optional[str] = ..., account_id: _Optional[str] = ..., order_id: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., asset_type: _Optional[str] = ..., wallet_address: _Optional[str] = ..., side: _Optional[str] = ...) -> None: ...

class CancelBatchOrdersRequest(_message.Message):
    __slots__ = ["exchange", "account_id", "orders_id", "pair", "asset_type", "wallet_address", "side"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ORDERS_ID_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    WALLET_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    account_id: str
    orders_id: str
    pair: CurrencyPair
    asset_type: str
    wallet_address: str
    side: str
    def __init__(self, exchange: _Optional[str] = ..., account_id: _Optional[str] = ..., orders_id: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., asset_type: _Optional[str] = ..., wallet_address: _Optional[str] = ..., side: _Optional[str] = ...) -> None: ...

class Orders(_message.Message):
    __slots__ = ["exchange", "order_status"]
    class OrderStatusEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ORDER_STATUS_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    order_status: _containers.ScalarMap[str, str]
    def __init__(self, exchange: _Optional[str] = ..., order_status: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CancelBatchOrdersResponse(_message.Message):
    __slots__ = ["orders"]
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    orders: _containers.RepeatedCompositeFieldContainer[Orders]
    def __init__(self, orders: _Optional[_Iterable[_Union[Orders, _Mapping]]] = ...) -> None: ...

class CancelAllOrdersRequest(_message.Message):
    __slots__ = ["exchange"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    def __init__(self, exchange: _Optional[str] = ...) -> None: ...

class CancelAllOrdersResponse(_message.Message):
    __slots__ = ["orders", "count"]
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    orders: _containers.RepeatedCompositeFieldContainer[Orders]
    count: int
    def __init__(self, orders: _Optional[_Iterable[_Union[Orders, _Mapping]]] = ..., count: _Optional[int] = ...) -> None: ...

class GetEventsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ConditionParams(_message.Message):
    __slots__ = ["condition", "price", "check_bids", "check_asks", "orderbook_amount"]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CHECK_BIDS_FIELD_NUMBER: _ClassVar[int]
    CHECK_ASKS_FIELD_NUMBER: _ClassVar[int]
    ORDERBOOK_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    condition: str
    price: float
    check_bids: bool
    check_asks: bool
    orderbook_amount: float
    def __init__(self, condition: _Optional[str] = ..., price: _Optional[float] = ..., check_bids: bool = ..., check_asks: bool = ..., orderbook_amount: _Optional[float] = ...) -> None: ...

class GetEventsResponse(_message.Message):
    __slots__ = ["id", "exchange", "item", "condition_params", "pair", "action", "executed"]
    ID_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    CONDITION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    EXECUTED_FIELD_NUMBER: _ClassVar[int]
    id: int
    exchange: str
    item: str
    condition_params: ConditionParams
    pair: CurrencyPair
    action: str
    executed: bool
    def __init__(self, id: _Optional[int] = ..., exchange: _Optional[str] = ..., item: _Optional[str] = ..., condition_params: _Optional[_Union[ConditionParams, _Mapping]] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., action: _Optional[str] = ..., executed: bool = ...) -> None: ...

class AddEventRequest(_message.Message):
    __slots__ = ["exchange", "item", "condition_params", "pair", "asset_type", "action"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    CONDITION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    item: str
    condition_params: ConditionParams
    pair: CurrencyPair
    asset_type: str
    action: str
    def __init__(self, exchange: _Optional[str] = ..., item: _Optional[str] = ..., condition_params: _Optional[_Union[ConditionParams, _Mapping]] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., asset_type: _Optional[str] = ..., action: _Optional[str] = ...) -> None: ...

class AddEventResponse(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class RemoveEventRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetCryptocurrencyDepositAddressesRequest(_message.Message):
    __slots__ = ["exchange"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    def __init__(self, exchange: _Optional[str] = ...) -> None: ...

class DepositAddress(_message.Message):
    __slots__ = ["address", "tag", "chain"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    CHAIN_FIELD_NUMBER: _ClassVar[int]
    address: str
    tag: str
    chain: str
    def __init__(self, address: _Optional[str] = ..., tag: _Optional[str] = ..., chain: _Optional[str] = ...) -> None: ...

class DepositAddresses(_message.Message):
    __slots__ = ["addresses"]
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    addresses: _containers.RepeatedCompositeFieldContainer[DepositAddress]
    def __init__(self, addresses: _Optional[_Iterable[_Union[DepositAddress, _Mapping]]] = ...) -> None: ...

class GetCryptocurrencyDepositAddressesResponse(_message.Message):
    __slots__ = ["addresses"]
    class AddressesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: DepositAddresses
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[DepositAddresses, _Mapping]] = ...) -> None: ...
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    addresses: _containers.MessageMap[str, DepositAddresses]
    def __init__(self, addresses: _Optional[_Mapping[str, DepositAddresses]] = ...) -> None: ...

class GetCryptocurrencyDepositAddressRequest(_message.Message):
    __slots__ = ["exchange", "cryptocurrency", "chain", "bypass"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    CRYPTOCURRENCY_FIELD_NUMBER: _ClassVar[int]
    CHAIN_FIELD_NUMBER: _ClassVar[int]
    BYPASS_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    cryptocurrency: str
    chain: str
    bypass: bool
    def __init__(self, exchange: _Optional[str] = ..., cryptocurrency: _Optional[str] = ..., chain: _Optional[str] = ..., bypass: bool = ...) -> None: ...

class GetCryptocurrencyDepositAddressResponse(_message.Message):
    __slots__ = ["address", "tag"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    address: str
    tag: str
    def __init__(self, address: _Optional[str] = ..., tag: _Optional[str] = ...) -> None: ...

class GetAvailableTransferChainsRequest(_message.Message):
    __slots__ = ["exchange", "cryptocurrency"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    CRYPTOCURRENCY_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    cryptocurrency: str
    def __init__(self, exchange: _Optional[str] = ..., cryptocurrency: _Optional[str] = ...) -> None: ...

class GetAvailableTransferChainsResponse(_message.Message):
    __slots__ = ["chains"]
    CHAINS_FIELD_NUMBER: _ClassVar[int]
    chains: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, chains: _Optional[_Iterable[str]] = ...) -> None: ...

class WithdrawFiatRequest(_message.Message):
    __slots__ = ["exchange", "currency", "amount", "description", "bank_account_id"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BANK_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    currency: str
    amount: float
    description: str
    bank_account_id: str
    def __init__(self, exchange: _Optional[str] = ..., currency: _Optional[str] = ..., amount: _Optional[float] = ..., description: _Optional[str] = ..., bank_account_id: _Optional[str] = ...) -> None: ...

class WithdrawCryptoRequest(_message.Message):
    __slots__ = ["exchange", "address", "address_tag", "currency", "amount", "fee", "description", "chain"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_TAG_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    FEE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CHAIN_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    address: str
    address_tag: str
    currency: str
    amount: float
    fee: float
    description: str
    chain: str
    def __init__(self, exchange: _Optional[str] = ..., address: _Optional[str] = ..., address_tag: _Optional[str] = ..., currency: _Optional[str] = ..., amount: _Optional[float] = ..., fee: _Optional[float] = ..., description: _Optional[str] = ..., chain: _Optional[str] = ...) -> None: ...

class WithdrawResponse(_message.Message):
    __slots__ = ["id", "status"]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: str
    def __init__(self, id: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class WithdrawalEventByIDRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class WithdrawalEventByIDResponse(_message.Message):
    __slots__ = ["event"]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: WithdrawalEventResponse
    def __init__(self, event: _Optional[_Union[WithdrawalEventResponse, _Mapping]] = ...) -> None: ...

class WithdrawalEventsByExchangeRequest(_message.Message):
    __slots__ = ["exchange", "id", "limit", "currency", "asset_type"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    id: str
    limit: int
    currency: str
    asset_type: str
    def __init__(self, exchange: _Optional[str] = ..., id: _Optional[str] = ..., limit: _Optional[int] = ..., currency: _Optional[str] = ..., asset_type: _Optional[str] = ...) -> None: ...

class WithdrawalEventsByDateRequest(_message.Message):
    __slots__ = ["exchange", "start", "end", "limit"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    start: str
    end: str
    limit: int
    def __init__(self, exchange: _Optional[str] = ..., start: _Optional[str] = ..., end: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class WithdrawalEventsByExchangeResponse(_message.Message):
    __slots__ = ["event"]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: _containers.RepeatedCompositeFieldContainer[WithdrawalEventResponse]
    def __init__(self, event: _Optional[_Iterable[_Union[WithdrawalEventResponse, _Mapping]]] = ...) -> None: ...

class WithdrawalEventResponse(_message.Message):
    __slots__ = ["id", "exchange", "request", "created_at", "updated_at"]
    ID_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    exchange: WithdrawlExchangeEvent
    request: WithdrawalRequestEvent
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., exchange: _Optional[_Union[WithdrawlExchangeEvent, _Mapping]] = ..., request: _Optional[_Union[WithdrawalRequestEvent, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class WithdrawlExchangeEvent(_message.Message):
    __slots__ = ["name", "id", "status"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    status: str
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class WithdrawalRequestEvent(_message.Message):
    __slots__ = ["currency", "description", "amount", "type", "fiat", "crypto"]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FIAT_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_FIELD_NUMBER: _ClassVar[int]
    currency: str
    description: str
    amount: float
    type: int
    fiat: FiatWithdrawalEvent
    crypto: CryptoWithdrawalEvent
    def __init__(self, currency: _Optional[str] = ..., description: _Optional[str] = ..., amount: _Optional[float] = ..., type: _Optional[int] = ..., fiat: _Optional[_Union[FiatWithdrawalEvent, _Mapping]] = ..., crypto: _Optional[_Union[CryptoWithdrawalEvent, _Mapping]] = ...) -> None: ...

class FiatWithdrawalEvent(_message.Message):
    __slots__ = ["bank_name", "account_name", "account_number", "bsb", "swift", "iban"]
    BANK_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BSB_FIELD_NUMBER: _ClassVar[int]
    SWIFT_FIELD_NUMBER: _ClassVar[int]
    IBAN_FIELD_NUMBER: _ClassVar[int]
    bank_name: str
    account_name: str
    account_number: str
    bsb: str
    swift: str
    iban: str
    def __init__(self, bank_name: _Optional[str] = ..., account_name: _Optional[str] = ..., account_number: _Optional[str] = ..., bsb: _Optional[str] = ..., swift: _Optional[str] = ..., iban: _Optional[str] = ...) -> None: ...

class CryptoWithdrawalEvent(_message.Message):
    __slots__ = ["address", "address_tag", "fee", "tx_id"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_TAG_FIELD_NUMBER: _ClassVar[int]
    FEE_FIELD_NUMBER: _ClassVar[int]
    TX_ID_FIELD_NUMBER: _ClassVar[int]
    address: str
    address_tag: str
    fee: float
    tx_id: str
    def __init__(self, address: _Optional[str] = ..., address_tag: _Optional[str] = ..., fee: _Optional[float] = ..., tx_id: _Optional[str] = ...) -> None: ...

class GetLoggerDetailsRequest(_message.Message):
    __slots__ = ["logger"]
    LOGGER_FIELD_NUMBER: _ClassVar[int]
    logger: str
    def __init__(self, logger: _Optional[str] = ...) -> None: ...

class GetLoggerDetailsResponse(_message.Message):
    __slots__ = ["info", "debug", "warn", "error"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    DEBUG_FIELD_NUMBER: _ClassVar[int]
    WARN_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    info: bool
    debug: bool
    warn: bool
    error: bool
    def __init__(self, info: bool = ..., debug: bool = ..., warn: bool = ..., error: bool = ...) -> None: ...

class SetLoggerDetailsRequest(_message.Message):
    __slots__ = ["logger", "level"]
    LOGGER_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    logger: str
    level: str
    def __init__(self, logger: _Optional[str] = ..., level: _Optional[str] = ...) -> None: ...

class GetExchangePairsRequest(_message.Message):
    __slots__ = ["exchange", "asset"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    asset: str
    def __init__(self, exchange: _Optional[str] = ..., asset: _Optional[str] = ...) -> None: ...

class GetExchangePairsResponse(_message.Message):
    __slots__ = ["supported_assets"]
    class SupportedAssetsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: PairsSupported
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[PairsSupported, _Mapping]] = ...) -> None: ...
    SUPPORTED_ASSETS_FIELD_NUMBER: _ClassVar[int]
    supported_assets: _containers.MessageMap[str, PairsSupported]
    def __init__(self, supported_assets: _Optional[_Mapping[str, PairsSupported]] = ...) -> None: ...

class SetExchangePairRequest(_message.Message):
    __slots__ = ["exchange", "asset_type", "pairs", "enable"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAIRS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    asset_type: str
    pairs: _containers.RepeatedCompositeFieldContainer[CurrencyPair]
    enable: bool
    def __init__(self, exchange: _Optional[str] = ..., asset_type: _Optional[str] = ..., pairs: _Optional[_Iterable[_Union[CurrencyPair, _Mapping]]] = ..., enable: bool = ...) -> None: ...

class GetOrderbookStreamRequest(_message.Message):
    __slots__ = ["exchange", "pair", "asset_type"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    pair: CurrencyPair
    asset_type: str
    def __init__(self, exchange: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., asset_type: _Optional[str] = ...) -> None: ...

class GetExchangeOrderbookStreamRequest(_message.Message):
    __slots__ = ["exchange"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    def __init__(self, exchange: _Optional[str] = ...) -> None: ...

class GetTickerStreamRequest(_message.Message):
    __slots__ = ["exchange", "pair", "asset_type"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    pair: CurrencyPair
    asset_type: str
    def __init__(self, exchange: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., asset_type: _Optional[str] = ...) -> None: ...

class GetExchangeTickerStreamRequest(_message.Message):
    __slots__ = ["exchange"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    def __init__(self, exchange: _Optional[str] = ...) -> None: ...

class GetAuditEventRequest(_message.Message):
    __slots__ = ["start_date", "end_date", "order_by", "limit", "offset"]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    start_date: str
    end_date: str
    order_by: str
    limit: int
    offset: int
    def __init__(self, start_date: _Optional[str] = ..., end_date: _Optional[str] = ..., order_by: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class GetAuditEventResponse(_message.Message):
    __slots__ = ["events"]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[AuditEvent]
    def __init__(self, events: _Optional[_Iterable[_Union[AuditEvent, _Mapping]]] = ...) -> None: ...

class GetSavedTradesRequest(_message.Message):
    __slots__ = ["exchange", "pair", "asset_type", "start", "end"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    pair: CurrencyPair
    asset_type: str
    start: str
    end: str
    def __init__(self, exchange: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., asset_type: _Optional[str] = ..., start: _Optional[str] = ..., end: _Optional[str] = ...) -> None: ...

class SavedTrades(_message.Message):
    __slots__ = ["price", "amount", "side", "timestamp", "trade_id"]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    price: float
    amount: float
    side: str
    timestamp: str
    trade_id: str
    def __init__(self, price: _Optional[float] = ..., amount: _Optional[float] = ..., side: _Optional[str] = ..., timestamp: _Optional[str] = ..., trade_id: _Optional[str] = ...) -> None: ...

class SavedTradesResponse(_message.Message):
    __slots__ = ["exchange_name", "asset", "pair", "trades"]
    EXCHANGE_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    TRADES_FIELD_NUMBER: _ClassVar[int]
    exchange_name: str
    asset: str
    pair: CurrencyPair
    trades: _containers.RepeatedCompositeFieldContainer[SavedTrades]
    def __init__(self, exchange_name: _Optional[str] = ..., asset: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., trades: _Optional[_Iterable[_Union[SavedTrades, _Mapping]]] = ...) -> None: ...

class ConvertTradesToCandlesRequest(_message.Message):
    __slots__ = ["exchange", "pair", "asset_type", "start", "end", "time_interval", "sync", "force"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    TIME_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    SYNC_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    pair: CurrencyPair
    asset_type: str
    start: str
    end: str
    time_interval: int
    sync: bool
    force: bool
    def __init__(self, exchange: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., asset_type: _Optional[str] = ..., start: _Optional[str] = ..., end: _Optional[str] = ..., time_interval: _Optional[int] = ..., sync: bool = ..., force: bool = ...) -> None: ...

class GetHistoricCandlesRequest(_message.Message):
    __slots__ = ["exchange", "pair", "asset_type", "start", "end", "time_interval", "ex_request", "sync", "use_db", "fill_missing_with_trades", "force"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    TIME_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    EX_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SYNC_FIELD_NUMBER: _ClassVar[int]
    USE_DB_FIELD_NUMBER: _ClassVar[int]
    FILL_MISSING_WITH_TRADES_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    pair: CurrencyPair
    asset_type: str
    start: str
    end: str
    time_interval: int
    ex_request: bool
    sync: bool
    use_db: bool
    fill_missing_with_trades: bool
    force: bool
    def __init__(self, exchange: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., asset_type: _Optional[str] = ..., start: _Optional[str] = ..., end: _Optional[str] = ..., time_interval: _Optional[int] = ..., ex_request: bool = ..., sync: bool = ..., use_db: bool = ..., fill_missing_with_trades: bool = ..., force: bool = ...) -> None: ...

class GetHistoricCandlesResponse(_message.Message):
    __slots__ = ["exchange", "pair", "start", "end", "interval", "candle"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    CANDLE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    pair: CurrencyPair
    start: str
    end: str
    interval: str
    candle: _containers.RepeatedCompositeFieldContainer[Candle]
    def __init__(self, exchange: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., start: _Optional[str] = ..., end: _Optional[str] = ..., interval: _Optional[str] = ..., candle: _Optional[_Iterable[_Union[Candle, _Mapping]]] = ...) -> None: ...

class Candle(_message.Message):
    __slots__ = ["time", "low", "high", "open", "close", "volume", "is_partial"]
    TIME_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    OPEN_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    IS_PARTIAL_FIELD_NUMBER: _ClassVar[int]
    time: str
    low: float
    high: float
    open: float
    close: float
    volume: float
    is_partial: bool
    def __init__(self, time: _Optional[str] = ..., low: _Optional[float] = ..., high: _Optional[float] = ..., open: _Optional[float] = ..., close: _Optional[float] = ..., volume: _Optional[float] = ..., is_partial: bool = ...) -> None: ...

class AuditEvent(_message.Message):
    __slots__ = ["type", "identifier", "message", "timestamp"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    type: str
    identifier: str
    message: str
    timestamp: str
    def __init__(self, type: _Optional[str] = ..., identifier: _Optional[str] = ..., message: _Optional[str] = ..., timestamp: _Optional[str] = ...) -> None: ...

class GCTScript(_message.Message):
    __slots__ = ["uuid", "name", "path", "next_run"]
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    NEXT_RUN_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    name: str
    path: str
    next_run: str
    def __init__(self, uuid: _Optional[str] = ..., name: _Optional[str] = ..., path: _Optional[str] = ..., next_run: _Optional[str] = ...) -> None: ...

class GCTScriptExecuteRequest(_message.Message):
    __slots__ = ["script"]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    script: GCTScript
    def __init__(self, script: _Optional[_Union[GCTScript, _Mapping]] = ...) -> None: ...

class GCTScriptStopRequest(_message.Message):
    __slots__ = ["script"]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    script: GCTScript
    def __init__(self, script: _Optional[_Union[GCTScript, _Mapping]] = ...) -> None: ...

class GCTScriptStopAllRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GCTScriptStatusRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GCTScriptListAllRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GCTScriptUploadRequest(_message.Message):
    __slots__ = ["script_name", "script_data", "data", "archived", "overwrite"]
    SCRIPT_NAME_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_DATA_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    script_name: str
    script_data: str
    data: bytes
    archived: bool
    overwrite: bool
    def __init__(self, script_name: _Optional[str] = ..., script_data: _Optional[str] = ..., data: _Optional[bytes] = ..., archived: bool = ..., overwrite: bool = ...) -> None: ...

class GCTScriptReadScriptRequest(_message.Message):
    __slots__ = ["script"]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    script: GCTScript
    def __init__(self, script: _Optional[_Union[GCTScript, _Mapping]] = ...) -> None: ...

class GCTScriptQueryRequest(_message.Message):
    __slots__ = ["script"]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    script: GCTScript
    def __init__(self, script: _Optional[_Union[GCTScript, _Mapping]] = ...) -> None: ...

class GCTScriptAutoLoadRequest(_message.Message):
    __slots__ = ["script", "status"]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    script: str
    status: bool
    def __init__(self, script: _Optional[str] = ..., status: bool = ...) -> None: ...

class GCTScriptStatusResponse(_message.Message):
    __slots__ = ["status", "scripts"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SCRIPTS_FIELD_NUMBER: _ClassVar[int]
    status: str
    scripts: _containers.RepeatedCompositeFieldContainer[GCTScript]
    def __init__(self, status: _Optional[str] = ..., scripts: _Optional[_Iterable[_Union[GCTScript, _Mapping]]] = ...) -> None: ...

class GCTScriptQueryResponse(_message.Message):
    __slots__ = ["status", "script", "data"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: str
    script: GCTScript
    data: str
    def __init__(self, status: _Optional[str] = ..., script: _Optional[_Union[GCTScript, _Mapping]] = ..., data: _Optional[str] = ...) -> None: ...

class GenericResponse(_message.Message):
    __slots__ = ["status", "data"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: str
    data: str
    def __init__(self, status: _Optional[str] = ..., data: _Optional[str] = ...) -> None: ...

class SetExchangeAssetRequest(_message.Message):
    __slots__ = ["exchange", "asset", "enable"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    asset: str
    enable: bool
    def __init__(self, exchange: _Optional[str] = ..., asset: _Optional[str] = ..., enable: bool = ...) -> None: ...

class SetExchangeAllPairsRequest(_message.Message):
    __slots__ = ["exchange", "enable"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    enable: bool
    def __init__(self, exchange: _Optional[str] = ..., enable: bool = ...) -> None: ...

class UpdateExchangeSupportedPairsRequest(_message.Message):
    __slots__ = ["exchange"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    def __init__(self, exchange: _Optional[str] = ...) -> None: ...

class GetExchangeAssetsRequest(_message.Message):
    __slots__ = ["exchange"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    def __init__(self, exchange: _Optional[str] = ...) -> None: ...

class GetExchangeAssetsResponse(_message.Message):
    __slots__ = ["assets"]
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    assets: str
    def __init__(self, assets: _Optional[str] = ...) -> None: ...

class WebsocketGetInfoRequest(_message.Message):
    __slots__ = ["exchange"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    def __init__(self, exchange: _Optional[str] = ...) -> None: ...

class WebsocketGetInfoResponse(_message.Message):
    __slots__ = ["exchange", "supported", "enabled", "authenticated_supported", "authenticated", "running_url", "proxy_address"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATED_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATED_FIELD_NUMBER: _ClassVar[int]
    RUNNING_URL_FIELD_NUMBER: _ClassVar[int]
    PROXY_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    supported: bool
    enabled: bool
    authenticated_supported: bool
    authenticated: bool
    running_url: str
    proxy_address: str
    def __init__(self, exchange: _Optional[str] = ..., supported: bool = ..., enabled: bool = ..., authenticated_supported: bool = ..., authenticated: bool = ..., running_url: _Optional[str] = ..., proxy_address: _Optional[str] = ...) -> None: ...

class WebsocketSetEnabledRequest(_message.Message):
    __slots__ = ["exchange", "enable"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    enable: bool
    def __init__(self, exchange: _Optional[str] = ..., enable: bool = ...) -> None: ...

class WebsocketGetSubscriptionsRequest(_message.Message):
    __slots__ = ["exchange"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    def __init__(self, exchange: _Optional[str] = ...) -> None: ...

class WebsocketSubscription(_message.Message):
    __slots__ = ["channel", "currency", "asset", "params"]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    channel: str
    currency: str
    asset: str
    params: str
    def __init__(self, channel: _Optional[str] = ..., currency: _Optional[str] = ..., asset: _Optional[str] = ..., params: _Optional[str] = ...) -> None: ...

class WebsocketGetSubscriptionsResponse(_message.Message):
    __slots__ = ["exchange", "subscriptions"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    subscriptions: _containers.RepeatedCompositeFieldContainer[WebsocketSubscription]
    def __init__(self, exchange: _Optional[str] = ..., subscriptions: _Optional[_Iterable[_Union[WebsocketSubscription, _Mapping]]] = ...) -> None: ...

class WebsocketSetProxyRequest(_message.Message):
    __slots__ = ["exchange", "proxy"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    PROXY_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    proxy: str
    def __init__(self, exchange: _Optional[str] = ..., proxy: _Optional[str] = ...) -> None: ...

class WebsocketSetURLRequest(_message.Message):
    __slots__ = ["exchange", "url"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    url: str
    def __init__(self, exchange: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class FindMissingCandlePeriodsRequest(_message.Message):
    __slots__ = ["exchange_name", "asset_type", "pair", "interval", "start", "end"]
    EXCHANGE_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    exchange_name: str
    asset_type: str
    pair: CurrencyPair
    interval: int
    start: str
    end: str
    def __init__(self, exchange_name: _Optional[str] = ..., asset_type: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., interval: _Optional[int] = ..., start: _Optional[str] = ..., end: _Optional[str] = ...) -> None: ...

class FindMissingTradePeriodsRequest(_message.Message):
    __slots__ = ["exchange_name", "asset_type", "pair", "start", "end"]
    EXCHANGE_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    exchange_name: str
    asset_type: str
    pair: CurrencyPair
    start: str
    end: str
    def __init__(self, exchange_name: _Optional[str] = ..., asset_type: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., start: _Optional[str] = ..., end: _Optional[str] = ...) -> None: ...

class FindMissingIntervalsResponse(_message.Message):
    __slots__ = ["exchange_name", "asset_type", "pair", "missing_periods", "status"]
    EXCHANGE_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    MISSING_PERIODS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    exchange_name: str
    asset_type: str
    pair: CurrencyPair
    missing_periods: _containers.RepeatedScalarFieldContainer[str]
    status: str
    def __init__(self, exchange_name: _Optional[str] = ..., asset_type: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., missing_periods: _Optional[_Iterable[str]] = ..., status: _Optional[str] = ...) -> None: ...

class SetExchangeTradeProcessingRequest(_message.Message):
    __slots__ = ["exchange", "status"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    status: bool
    def __init__(self, exchange: _Optional[str] = ..., status: bool = ...) -> None: ...

class UpsertDataHistoryJobRequest(_message.Message):
    __slots__ = ["nickname", "exchange", "asset", "pair", "start_date", "end_date", "interval", "request_size_limit", "data_type", "max_retry_attempts", "batch_size", "insert_only", "conversion_interval", "overwrite_existing_data", "prerequisite_job_nickname", "decimal_place_comparison", "secondary_exchange_name", "issue_tolerance_percentage", "replace_on_issue"]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SIZE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAX_RETRY_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    INSERT_ONLY_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_EXISTING_DATA_FIELD_NUMBER: _ClassVar[int]
    PREREQUISITE_JOB_NICKNAME_FIELD_NUMBER: _ClassVar[int]
    DECIMAL_PLACE_COMPARISON_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_EXCHANGE_NAME_FIELD_NUMBER: _ClassVar[int]
    ISSUE_TOLERANCE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    REPLACE_ON_ISSUE_FIELD_NUMBER: _ClassVar[int]
    nickname: str
    exchange: str
    asset: str
    pair: CurrencyPair
    start_date: str
    end_date: str
    interval: int
    request_size_limit: int
    data_type: int
    max_retry_attempts: int
    batch_size: int
    insert_only: bool
    conversion_interval: int
    overwrite_existing_data: bool
    prerequisite_job_nickname: str
    decimal_place_comparison: int
    secondary_exchange_name: str
    issue_tolerance_percentage: float
    replace_on_issue: bool
    def __init__(self, nickname: _Optional[str] = ..., exchange: _Optional[str] = ..., asset: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., start_date: _Optional[str] = ..., end_date: _Optional[str] = ..., interval: _Optional[int] = ..., request_size_limit: _Optional[int] = ..., data_type: _Optional[int] = ..., max_retry_attempts: _Optional[int] = ..., batch_size: _Optional[int] = ..., insert_only: bool = ..., conversion_interval: _Optional[int] = ..., overwrite_existing_data: bool = ..., prerequisite_job_nickname: _Optional[str] = ..., decimal_place_comparison: _Optional[int] = ..., secondary_exchange_name: _Optional[str] = ..., issue_tolerance_percentage: _Optional[float] = ..., replace_on_issue: bool = ...) -> None: ...

class InsertSequentialJobsRequest(_message.Message):
    __slots__ = ["jobs"]
    JOBS_FIELD_NUMBER: _ClassVar[int]
    jobs: _containers.RepeatedCompositeFieldContainer[UpsertDataHistoryJobRequest]
    def __init__(self, jobs: _Optional[_Iterable[_Union[UpsertDataHistoryJobRequest, _Mapping]]] = ...) -> None: ...

class InsertSequentialJobsResponse(_message.Message):
    __slots__ = ["jobs"]
    JOBS_FIELD_NUMBER: _ClassVar[int]
    jobs: _containers.RepeatedCompositeFieldContainer[UpsertDataHistoryJobResponse]
    def __init__(self, jobs: _Optional[_Iterable[_Union[UpsertDataHistoryJobResponse, _Mapping]]] = ...) -> None: ...

class UpsertDataHistoryJobResponse(_message.Message):
    __slots__ = ["message", "job_id"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    message: str
    job_id: str
    def __init__(self, message: _Optional[str] = ..., job_id: _Optional[str] = ...) -> None: ...

class GetDataHistoryJobDetailsRequest(_message.Message):
    __slots__ = ["id", "nickname", "full_details"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    FULL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    id: str
    nickname: str
    full_details: bool
    def __init__(self, id: _Optional[str] = ..., nickname: _Optional[str] = ..., full_details: bool = ...) -> None: ...

class DataHistoryJob(_message.Message):
    __slots__ = ["id", "nickname", "exchange", "asset", "pair", "start_date", "end_date", "interval", "request_size_limit", "max_retry_attempts", "batch_size", "status", "data_type", "conversion_interval", "overwrite_existing_data", "prerequisite_job_nickname", "decimal_place_comparison", "secondary_exchange_name", "issue_tolerance_percentage", "replace_on_issue", "job_results", "result_summaries"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SIZE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MAX_RETRY_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_EXISTING_DATA_FIELD_NUMBER: _ClassVar[int]
    PREREQUISITE_JOB_NICKNAME_FIELD_NUMBER: _ClassVar[int]
    DECIMAL_PLACE_COMPARISON_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_EXCHANGE_NAME_FIELD_NUMBER: _ClassVar[int]
    ISSUE_TOLERANCE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    REPLACE_ON_ISSUE_FIELD_NUMBER: _ClassVar[int]
    JOB_RESULTS_FIELD_NUMBER: _ClassVar[int]
    RESULT_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    nickname: str
    exchange: str
    asset: str
    pair: CurrencyPair
    start_date: str
    end_date: str
    interval: int
    request_size_limit: int
    max_retry_attempts: int
    batch_size: int
    status: str
    data_type: str
    conversion_interval: int
    overwrite_existing_data: bool
    prerequisite_job_nickname: str
    decimal_place_comparison: int
    secondary_exchange_name: str
    issue_tolerance_percentage: float
    replace_on_issue: bool
    job_results: _containers.RepeatedCompositeFieldContainer[DataHistoryJobResult]
    result_summaries: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., nickname: _Optional[str] = ..., exchange: _Optional[str] = ..., asset: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., start_date: _Optional[str] = ..., end_date: _Optional[str] = ..., interval: _Optional[int] = ..., request_size_limit: _Optional[int] = ..., max_retry_attempts: _Optional[int] = ..., batch_size: _Optional[int] = ..., status: _Optional[str] = ..., data_type: _Optional[str] = ..., conversion_interval: _Optional[int] = ..., overwrite_existing_data: bool = ..., prerequisite_job_nickname: _Optional[str] = ..., decimal_place_comparison: _Optional[int] = ..., secondary_exchange_name: _Optional[str] = ..., issue_tolerance_percentage: _Optional[float] = ..., replace_on_issue: bool = ..., job_results: _Optional[_Iterable[_Union[DataHistoryJobResult, _Mapping]]] = ..., result_summaries: _Optional[_Iterable[str]] = ...) -> None: ...

class DataHistoryJobResult(_message.Message):
    __slots__ = ["start_date", "end_date", "has_data", "message", "run_date"]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    HAS_DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RUN_DATE_FIELD_NUMBER: _ClassVar[int]
    start_date: str
    end_date: str
    has_data: bool
    message: str
    run_date: str
    def __init__(self, start_date: _Optional[str] = ..., end_date: _Optional[str] = ..., has_data: bool = ..., message: _Optional[str] = ..., run_date: _Optional[str] = ...) -> None: ...

class DataHistoryJobs(_message.Message):
    __slots__ = ["results"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[DataHistoryJob]
    def __init__(self, results: _Optional[_Iterable[_Union[DataHistoryJob, _Mapping]]] = ...) -> None: ...

class GetDataHistoryJobsBetweenRequest(_message.Message):
    __slots__ = ["start_date", "end_date"]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    start_date: str
    end_date: str
    def __init__(self, start_date: _Optional[str] = ..., end_date: _Optional[str] = ...) -> None: ...

class SetDataHistoryJobStatusRequest(_message.Message):
    __slots__ = ["id", "nickname", "status"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    nickname: str
    status: int
    def __init__(self, id: _Optional[str] = ..., nickname: _Optional[str] = ..., status: _Optional[int] = ...) -> None: ...

class UpdateDataHistoryJobPrerequisiteRequest(_message.Message):
    __slots__ = ["nickname", "prerequisite_job_nickname"]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PREREQUISITE_JOB_NICKNAME_FIELD_NUMBER: _ClassVar[int]
    nickname: str
    prerequisite_job_nickname: str
    def __init__(self, nickname: _Optional[str] = ..., prerequisite_job_nickname: _Optional[str] = ...) -> None: ...

class ModifyOrderRequest(_message.Message):
    __slots__ = ["exchange", "order_id", "pair", "asset", "amount", "price"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    order_id: str
    pair: CurrencyPair
    asset: str
    amount: float
    price: float
    def __init__(self, exchange: _Optional[str] = ..., order_id: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., asset: _Optional[str] = ..., amount: _Optional[float] = ..., price: _Optional[float] = ...) -> None: ...

class ModifyOrderResponse(_message.Message):
    __slots__ = ["modified_order_id"]
    MODIFIED_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    modified_order_id: str
    def __init__(self, modified_order_id: _Optional[str] = ...) -> None: ...

class CurrencyStateGetAllRequest(_message.Message):
    __slots__ = ["exchange"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    def __init__(self, exchange: _Optional[str] = ...) -> None: ...

class CurrencyStateTradingRequest(_message.Message):
    __slots__ = ["exchange", "code", "asset"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    code: str
    asset: str
    def __init__(self, exchange: _Optional[str] = ..., code: _Optional[str] = ..., asset: _Optional[str] = ...) -> None: ...

class CurrencyStateTradingPairRequest(_message.Message):
    __slots__ = ["exchange", "pair", "asset"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    pair: str
    asset: str
    def __init__(self, exchange: _Optional[str] = ..., pair: _Optional[str] = ..., asset: _Optional[str] = ...) -> None: ...

class CurrencyStateWithdrawRequest(_message.Message):
    __slots__ = ["exchange", "code", "asset"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    code: str
    asset: str
    def __init__(self, exchange: _Optional[str] = ..., code: _Optional[str] = ..., asset: _Optional[str] = ...) -> None: ...

class CurrencyStateDepositRequest(_message.Message):
    __slots__ = ["exchange", "code", "asset"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    code: str
    asset: str
    def __init__(self, exchange: _Optional[str] = ..., code: _Optional[str] = ..., asset: _Optional[str] = ...) -> None: ...

class CurrencyStateResponse(_message.Message):
    __slots__ = ["currency_states"]
    CURRENCY_STATES_FIELD_NUMBER: _ClassVar[int]
    currency_states: _containers.RepeatedCompositeFieldContainer[CurrencyState]
    def __init__(self, currency_states: _Optional[_Iterable[_Union[CurrencyState, _Mapping]]] = ...) -> None: ...

class CurrencyState(_message.Message):
    __slots__ = ["currency", "asset", "withdraw_enabled", "deposit_enabled", "trading_enabled"]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    WITHDRAW_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DEPOSIT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TRADING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    currency: str
    asset: str
    withdraw_enabled: bool
    deposit_enabled: bool
    trading_enabled: bool
    def __init__(self, currency: _Optional[str] = ..., asset: _Optional[str] = ..., withdraw_enabled: bool = ..., deposit_enabled: bool = ..., trading_enabled: bool = ...) -> None: ...

class FundingRate(_message.Message):
    __slots__ = ["date", "rate", "payment"]
    DATE_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_FIELD_NUMBER: _ClassVar[int]
    date: str
    rate: str
    payment: str
    def __init__(self, date: _Optional[str] = ..., rate: _Optional[str] = ..., payment: _Optional[str] = ...) -> None: ...

class FundingData(_message.Message):
    __slots__ = ["exchange", "asset", "pair", "payment_currency", "start_date", "end_date", "rates", "latest_rate", "upcoming_rate", "payment_sum", "payment_message", "time_of_next_rate"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    RATES_FIELD_NUMBER: _ClassVar[int]
    LATEST_RATE_FIELD_NUMBER: _ClassVar[int]
    UPCOMING_RATE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_SUM_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIME_OF_NEXT_RATE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    asset: str
    pair: CurrencyPair
    payment_currency: str
    start_date: str
    end_date: str
    rates: _containers.RepeatedCompositeFieldContainer[FundingRate]
    latest_rate: FundingRate
    upcoming_rate: FundingRate
    payment_sum: str
    payment_message: str
    time_of_next_rate: str
    def __init__(self, exchange: _Optional[str] = ..., asset: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., payment_currency: _Optional[str] = ..., start_date: _Optional[str] = ..., end_date: _Optional[str] = ..., rates: _Optional[_Iterable[_Union[FundingRate, _Mapping]]] = ..., latest_rate: _Optional[_Union[FundingRate, _Mapping]] = ..., upcoming_rate: _Optional[_Union[FundingRate, _Mapping]] = ..., payment_sum: _Optional[str] = ..., payment_message: _Optional[str] = ..., time_of_next_rate: _Optional[str] = ...) -> None: ...

class FuturesPositionStats(_message.Message):
    __slots__ = ["maintenance_margin_requirement", "initial_margin_requirement", "estimated_liquidation_price", "collateral_used", "mark_price", "current_size", "break_even_price", "average_open_price", "recent_pnl", "margin_fraction", "free_collateral", "total_collateral"]
    MAINTENANCE_MARGIN_REQUIREMENT_FIELD_NUMBER: _ClassVar[int]
    INITIAL_MARGIN_REQUIREMENT_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_LIQUIDATION_PRICE_FIELD_NUMBER: _ClassVar[int]
    COLLATERAL_USED_FIELD_NUMBER: _ClassVar[int]
    MARK_PRICE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SIZE_FIELD_NUMBER: _ClassVar[int]
    BREAK_EVEN_PRICE_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_OPEN_PRICE_FIELD_NUMBER: _ClassVar[int]
    RECENT_PNL_FIELD_NUMBER: _ClassVar[int]
    MARGIN_FRACTION_FIELD_NUMBER: _ClassVar[int]
    FREE_COLLATERAL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COLLATERAL_FIELD_NUMBER: _ClassVar[int]
    maintenance_margin_requirement: str
    initial_margin_requirement: str
    estimated_liquidation_price: str
    collateral_used: str
    mark_price: str
    current_size: str
    break_even_price: str
    average_open_price: str
    recent_pnl: str
    margin_fraction: str
    free_collateral: str
    total_collateral: str
    def __init__(self, maintenance_margin_requirement: _Optional[str] = ..., initial_margin_requirement: _Optional[str] = ..., estimated_liquidation_price: _Optional[str] = ..., collateral_used: _Optional[str] = ..., mark_price: _Optional[str] = ..., current_size: _Optional[str] = ..., break_even_price: _Optional[str] = ..., average_open_price: _Optional[str] = ..., recent_pnl: _Optional[str] = ..., margin_fraction: _Optional[str] = ..., free_collateral: _Optional[str] = ..., total_collateral: _Optional[str] = ...) -> None: ...

class FuturePosition(_message.Message):
    __slots__ = ["exchange", "asset", "pair", "status", "opening_date", "opening_direction", "opening_price", "opening_size", "current_direction", "current_price", "current_size", "unrealised_pnl", "realised_pnl", "closing_date", "order_count", "orders", "position_stats", "funding_data"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    OPENING_DATE_FIELD_NUMBER: _ClassVar[int]
    OPENING_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    OPENING_PRICE_FIELD_NUMBER: _ClassVar[int]
    OPENING_SIZE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PRICE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SIZE_FIELD_NUMBER: _ClassVar[int]
    UNREALISED_PNL_FIELD_NUMBER: _ClassVar[int]
    REALISED_PNL_FIELD_NUMBER: _ClassVar[int]
    CLOSING_DATE_FIELD_NUMBER: _ClassVar[int]
    ORDER_COUNT_FIELD_NUMBER: _ClassVar[int]
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    POSITION_STATS_FIELD_NUMBER: _ClassVar[int]
    FUNDING_DATA_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    asset: str
    pair: CurrencyPair
    status: str
    opening_date: str
    opening_direction: str
    opening_price: str
    opening_size: str
    current_direction: str
    current_price: str
    current_size: str
    unrealised_pnl: str
    realised_pnl: str
    closing_date: str
    order_count: int
    orders: _containers.RepeatedCompositeFieldContainer[OrderDetails]
    position_stats: FuturesPositionStats
    funding_data: FundingData
    def __init__(self, exchange: _Optional[str] = ..., asset: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., status: _Optional[str] = ..., opening_date: _Optional[str] = ..., opening_direction: _Optional[str] = ..., opening_price: _Optional[str] = ..., opening_size: _Optional[str] = ..., current_direction: _Optional[str] = ..., current_price: _Optional[str] = ..., current_size: _Optional[str] = ..., unrealised_pnl: _Optional[str] = ..., realised_pnl: _Optional[str] = ..., closing_date: _Optional[str] = ..., order_count: _Optional[int] = ..., orders: _Optional[_Iterable[_Union[OrderDetails, _Mapping]]] = ..., position_stats: _Optional[_Union[FuturesPositionStats, _Mapping]] = ..., funding_data: _Optional[_Union[FundingData, _Mapping]] = ...) -> None: ...

class GetManagedPositionRequest(_message.Message):
    __slots__ = ["exchange", "asset", "pair", "include_full_order_data", "get_funding_payments", "include_full_funding_rates", "include_predicted_rate"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FULL_ORDER_DATA_FIELD_NUMBER: _ClassVar[int]
    GET_FUNDING_PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FULL_FUNDING_RATES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PREDICTED_RATE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    asset: str
    pair: CurrencyPair
    include_full_order_data: bool
    get_funding_payments: bool
    include_full_funding_rates: bool
    include_predicted_rate: bool
    def __init__(self, exchange: _Optional[str] = ..., asset: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., include_full_order_data: bool = ..., get_funding_payments: bool = ..., include_full_funding_rates: bool = ..., include_predicted_rate: bool = ...) -> None: ...

class GetAllManagedPositionsRequest(_message.Message):
    __slots__ = ["include_full_order_data", "get_funding_payments", "include_full_funding_rates", "include_predicted_rate"]
    INCLUDE_FULL_ORDER_DATA_FIELD_NUMBER: _ClassVar[int]
    GET_FUNDING_PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FULL_FUNDING_RATES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PREDICTED_RATE_FIELD_NUMBER: _ClassVar[int]
    include_full_order_data: bool
    get_funding_payments: bool
    include_full_funding_rates: bool
    include_predicted_rate: bool
    def __init__(self, include_full_order_data: bool = ..., get_funding_payments: bool = ..., include_full_funding_rates: bool = ..., include_predicted_rate: bool = ...) -> None: ...

class GetManagedPositionsResponse(_message.Message):
    __slots__ = ["positions"]
    POSITIONS_FIELD_NUMBER: _ClassVar[int]
    positions: _containers.RepeatedCompositeFieldContainer[FuturePosition]
    def __init__(self, positions: _Optional[_Iterable[_Union[FuturePosition, _Mapping]]] = ...) -> None: ...

class GetFuturesPositionsRequest(_message.Message):
    __slots__ = ["exchange", "asset", "pair", "start_date", "end_date", "status", "position_limit", "overwrite", "get_position_stats", "include_full_order_data", "get_funding_payments", "include_full_funding_rates", "include_predicted_rate"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    POSITION_LIMIT_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    GET_POSITION_STATS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FULL_ORDER_DATA_FIELD_NUMBER: _ClassVar[int]
    GET_FUNDING_PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FULL_FUNDING_RATES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PREDICTED_RATE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    asset: str
    pair: CurrencyPair
    start_date: str
    end_date: str
    status: str
    position_limit: int
    overwrite: bool
    get_position_stats: bool
    include_full_order_data: bool
    get_funding_payments: bool
    include_full_funding_rates: bool
    include_predicted_rate: bool
    def __init__(self, exchange: _Optional[str] = ..., asset: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., start_date: _Optional[str] = ..., end_date: _Optional[str] = ..., status: _Optional[str] = ..., position_limit: _Optional[int] = ..., overwrite: bool = ..., get_position_stats: bool = ..., include_full_order_data: bool = ..., get_funding_payments: bool = ..., include_full_funding_rates: bool = ..., include_predicted_rate: bool = ...) -> None: ...

class GetFuturesPositionsResponse(_message.Message):
    __slots__ = ["total_orders", "sub_account", "total_realised_pnl", "total_unrealised_pnl", "total_pnl", "positions"]
    TOTAL_ORDERS_FIELD_NUMBER: _ClassVar[int]
    SUB_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_REALISED_PNL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_UNREALISED_PNL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PNL_FIELD_NUMBER: _ClassVar[int]
    POSITIONS_FIELD_NUMBER: _ClassVar[int]
    total_orders: int
    sub_account: str
    total_realised_pnl: str
    total_unrealised_pnl: str
    total_pnl: str
    positions: _containers.RepeatedCompositeFieldContainer[FuturePosition]
    def __init__(self, total_orders: _Optional[int] = ..., sub_account: _Optional[str] = ..., total_realised_pnl: _Optional[str] = ..., total_unrealised_pnl: _Optional[str] = ..., total_pnl: _Optional[str] = ..., positions: _Optional[_Iterable[_Union[FuturePosition, _Mapping]]] = ...) -> None: ...

class GetCollateralRequest(_message.Message):
    __slots__ = ["exchange", "asset", "include_breakdown", "calculate_offline", "include_zero_values"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_BREAKDOWN_FIELD_NUMBER: _ClassVar[int]
    CALCULATE_OFFLINE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ZERO_VALUES_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    asset: str
    include_breakdown: bool
    calculate_offline: bool
    include_zero_values: bool
    def __init__(self, exchange: _Optional[str] = ..., asset: _Optional[str] = ..., include_breakdown: bool = ..., calculate_offline: bool = ..., include_zero_values: bool = ...) -> None: ...

class GetCollateralResponse(_message.Message):
    __slots__ = ["sub_account", "collateral_currency", "total_value_of_positive_spot_balances", "collateral_contributed_by_positive_spot_balances", "used_collateral", "used_breakdown", "available_collateral", "maintenance_collateral", "unrealised_pnl", "currency_breakdown", "position_breakdown"]
    SUB_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    COLLATERAL_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_VALUE_OF_POSITIVE_SPOT_BALANCES_FIELD_NUMBER: _ClassVar[int]
    COLLATERAL_CONTRIBUTED_BY_POSITIVE_SPOT_BALANCES_FIELD_NUMBER: _ClassVar[int]
    USED_COLLATERAL_FIELD_NUMBER: _ClassVar[int]
    USED_BREAKDOWN_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_COLLATERAL_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_COLLATERAL_FIELD_NUMBER: _ClassVar[int]
    UNREALISED_PNL_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_BREAKDOWN_FIELD_NUMBER: _ClassVar[int]
    POSITION_BREAKDOWN_FIELD_NUMBER: _ClassVar[int]
    sub_account: str
    collateral_currency: str
    total_value_of_positive_spot_balances: str
    collateral_contributed_by_positive_spot_balances: str
    used_collateral: str
    used_breakdown: CollateralUsedBreakdown
    available_collateral: str
    maintenance_collateral: str
    unrealised_pnl: str
    currency_breakdown: _containers.RepeatedCompositeFieldContainer[CollateralForCurrency]
    position_breakdown: _containers.RepeatedCompositeFieldContainer[CollateralByPosition]
    def __init__(self, sub_account: _Optional[str] = ..., collateral_currency: _Optional[str] = ..., total_value_of_positive_spot_balances: _Optional[str] = ..., collateral_contributed_by_positive_spot_balances: _Optional[str] = ..., used_collateral: _Optional[str] = ..., used_breakdown: _Optional[_Union[CollateralUsedBreakdown, _Mapping]] = ..., available_collateral: _Optional[str] = ..., maintenance_collateral: _Optional[str] = ..., unrealised_pnl: _Optional[str] = ..., currency_breakdown: _Optional[_Iterable[_Union[CollateralForCurrency, _Mapping]]] = ..., position_breakdown: _Optional[_Iterable[_Union[CollateralByPosition, _Mapping]]] = ...) -> None: ...

class CollateralForCurrency(_message.Message):
    __slots__ = ["currency", "excluded_from_collateral", "total_funds", "available_for_use_as_collateral", "approx_fair_market_value", "weighting", "collateral_contribution", "scaled_to_currency", "unrealised_pnl", "funds_in_use", "additional_collateral_used", "used_breakdown", "error"]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_FROM_COLLATERAL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FUNDS_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_FOR_USE_AS_COLLATERAL_FIELD_NUMBER: _ClassVar[int]
    APPROX_FAIR_MARKET_VALUE_FIELD_NUMBER: _ClassVar[int]
    WEIGHTING_FIELD_NUMBER: _ClassVar[int]
    COLLATERAL_CONTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    SCALED_TO_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    UNREALISED_PNL_FIELD_NUMBER: _ClassVar[int]
    FUNDS_IN_USE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_COLLATERAL_USED_FIELD_NUMBER: _ClassVar[int]
    USED_BREAKDOWN_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    currency: str
    excluded_from_collateral: bool
    total_funds: str
    available_for_use_as_collateral: str
    approx_fair_market_value: str
    weighting: str
    collateral_contribution: str
    scaled_to_currency: str
    unrealised_pnl: str
    funds_in_use: str
    additional_collateral_used: str
    used_breakdown: CollateralUsedBreakdown
    error: str
    def __init__(self, currency: _Optional[str] = ..., excluded_from_collateral: bool = ..., total_funds: _Optional[str] = ..., available_for_use_as_collateral: _Optional[str] = ..., approx_fair_market_value: _Optional[str] = ..., weighting: _Optional[str] = ..., collateral_contribution: _Optional[str] = ..., scaled_to_currency: _Optional[str] = ..., unrealised_pnl: _Optional[str] = ..., funds_in_use: _Optional[str] = ..., additional_collateral_used: _Optional[str] = ..., used_breakdown: _Optional[_Union[CollateralUsedBreakdown, _Mapping]] = ..., error: _Optional[str] = ...) -> None: ...

class CollateralByPosition(_message.Message):
    __slots__ = ["currency", "size", "open_order_size", "position_size", "mark_price", "required_margin", "total_collateral_used"]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    OPEN_ORDER_SIZE_FIELD_NUMBER: _ClassVar[int]
    POSITION_SIZE_FIELD_NUMBER: _ClassVar[int]
    MARK_PRICE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_MARGIN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COLLATERAL_USED_FIELD_NUMBER: _ClassVar[int]
    currency: str
    size: str
    open_order_size: str
    position_size: str
    mark_price: str
    required_margin: str
    total_collateral_used: str
    def __init__(self, currency: _Optional[str] = ..., size: _Optional[str] = ..., open_order_size: _Optional[str] = ..., position_size: _Optional[str] = ..., mark_price: _Optional[str] = ..., required_margin: _Optional[str] = ..., total_collateral_used: _Optional[str] = ...) -> None: ...

class CollateralUsedBreakdown(_message.Message):
    __slots__ = ["locked_in_stakes", "locked_in_nft_bids", "locked_in_fee_voucher", "locked_in_spot_margin_funding_offers", "locked_in_spot_orders", "locked_as_collateral", "used_in_futures", "used_in_spot_margin"]
    LOCKED_IN_STAKES_FIELD_NUMBER: _ClassVar[int]
    LOCKED_IN_NFT_BIDS_FIELD_NUMBER: _ClassVar[int]
    LOCKED_IN_FEE_VOUCHER_FIELD_NUMBER: _ClassVar[int]
    LOCKED_IN_SPOT_MARGIN_FUNDING_OFFERS_FIELD_NUMBER: _ClassVar[int]
    LOCKED_IN_SPOT_ORDERS_FIELD_NUMBER: _ClassVar[int]
    LOCKED_AS_COLLATERAL_FIELD_NUMBER: _ClassVar[int]
    USED_IN_FUTURES_FIELD_NUMBER: _ClassVar[int]
    USED_IN_SPOT_MARGIN_FIELD_NUMBER: _ClassVar[int]
    locked_in_stakes: str
    locked_in_nft_bids: str
    locked_in_fee_voucher: str
    locked_in_spot_margin_funding_offers: str
    locked_in_spot_orders: str
    locked_as_collateral: str
    used_in_futures: str
    used_in_spot_margin: str
    def __init__(self, locked_in_stakes: _Optional[str] = ..., locked_in_nft_bids: _Optional[str] = ..., locked_in_fee_voucher: _Optional[str] = ..., locked_in_spot_margin_funding_offers: _Optional[str] = ..., locked_in_spot_orders: _Optional[str] = ..., locked_as_collateral: _Optional[str] = ..., used_in_futures: _Optional[str] = ..., used_in_spot_margin: _Optional[str] = ...) -> None: ...

class GetFundingRatesRequest(_message.Message):
    __slots__ = ["exchange", "asset", "pair", "start_date", "end_date", "payment_currency", "include_predicted", "include_payments", "respect_history_limits"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PREDICTED_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    RESPECT_HISTORY_LIMITS_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    asset: str
    pair: CurrencyPair
    start_date: str
    end_date: str
    payment_currency: str
    include_predicted: bool
    include_payments: bool
    respect_history_limits: bool
    def __init__(self, exchange: _Optional[str] = ..., asset: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., start_date: _Optional[str] = ..., end_date: _Optional[str] = ..., payment_currency: _Optional[str] = ..., include_predicted: bool = ..., include_payments: bool = ..., respect_history_limits: bool = ...) -> None: ...

class GetFundingRatesResponse(_message.Message):
    __slots__ = ["rates"]
    RATES_FIELD_NUMBER: _ClassVar[int]
    rates: FundingData
    def __init__(self, rates: _Optional[_Union[FundingData, _Mapping]] = ...) -> None: ...

class GetLatestFundingRateRequest(_message.Message):
    __slots__ = ["exchange", "asset", "pair", "include_predicted"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PREDICTED_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    asset: str
    pair: CurrencyPair
    include_predicted: bool
    def __init__(self, exchange: _Optional[str] = ..., asset: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., include_predicted: bool = ...) -> None: ...

class GetLatestFundingRateResponse(_message.Message):
    __slots__ = ["rate"]
    RATE_FIELD_NUMBER: _ClassVar[int]
    rate: FundingData
    def __init__(self, rate: _Optional[_Union[FundingData, _Mapping]] = ...) -> None: ...

class ShutdownRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ShutdownResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetTechnicalAnalysisRequest(_message.Message):
    __slots__ = ["exchange", "pair", "asset_type", "algorithm_type", "interval", "start", "end", "period", "fast_period", "slow_period", "standard_deviation_up", "standard_deviation_down", "moving_average_type", "other_exchange", "other_pair", "other_asset_type"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_TYPE_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    FAST_PERIOD_FIELD_NUMBER: _ClassVar[int]
    SLOW_PERIOD_FIELD_NUMBER: _ClassVar[int]
    STANDARD_DEVIATION_UP_FIELD_NUMBER: _ClassVar[int]
    STANDARD_DEVIATION_DOWN_FIELD_NUMBER: _ClassVar[int]
    MOVING_AVERAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OTHER_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    OTHER_PAIR_FIELD_NUMBER: _ClassVar[int]
    OTHER_ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    pair: CurrencyPair
    asset_type: str
    algorithm_type: str
    interval: int
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    period: int
    fast_period: int
    slow_period: int
    standard_deviation_up: float
    standard_deviation_down: float
    moving_average_type: int
    other_exchange: str
    other_pair: CurrencyPair
    other_asset_type: str
    def __init__(self, exchange: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., asset_type: _Optional[str] = ..., algorithm_type: _Optional[str] = ..., interval: _Optional[int] = ..., start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., period: _Optional[int] = ..., fast_period: _Optional[int] = ..., slow_period: _Optional[int] = ..., standard_deviation_up: _Optional[float] = ..., standard_deviation_down: _Optional[float] = ..., moving_average_type: _Optional[int] = ..., other_exchange: _Optional[str] = ..., other_pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., other_asset_type: _Optional[str] = ...) -> None: ...

class ListOfSignals(_message.Message):
    __slots__ = ["signals"]
    SIGNALS_FIELD_NUMBER: _ClassVar[int]
    signals: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, signals: _Optional[_Iterable[float]] = ...) -> None: ...

class GetTechnicalAnalysisResponse(_message.Message):
    __slots__ = ["signals"]
    class SignalsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ListOfSignals
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ListOfSignals, _Mapping]] = ...) -> None: ...
    SIGNALS_FIELD_NUMBER: _ClassVar[int]
    signals: _containers.MessageMap[str, ListOfSignals]
    def __init__(self, signals: _Optional[_Mapping[str, ListOfSignals]] = ...) -> None: ...

class GetMarginRatesHistoryRequest(_message.Message):
    __slots__ = ["exchange", "asset", "currency", "start_date", "end_date", "get_predicted_rate", "get_lending_payments", "get_borrow_rates", "get_borrow_costs", "include_all_rates", "calculate_offline", "taker_fee_rate", "rates"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    GET_PREDICTED_RATE_FIELD_NUMBER: _ClassVar[int]
    GET_LENDING_PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    GET_BORROW_RATES_FIELD_NUMBER: _ClassVar[int]
    GET_BORROW_COSTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ALL_RATES_FIELD_NUMBER: _ClassVar[int]
    CALCULATE_OFFLINE_FIELD_NUMBER: _ClassVar[int]
    TAKER_FEE_RATE_FIELD_NUMBER: _ClassVar[int]
    RATES_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    asset: str
    currency: str
    start_date: str
    end_date: str
    get_predicted_rate: bool
    get_lending_payments: bool
    get_borrow_rates: bool
    get_borrow_costs: bool
    include_all_rates: bool
    calculate_offline: bool
    taker_fee_rate: str
    rates: _containers.RepeatedCompositeFieldContainer[MarginRate]
    def __init__(self, exchange: _Optional[str] = ..., asset: _Optional[str] = ..., currency: _Optional[str] = ..., start_date: _Optional[str] = ..., end_date: _Optional[str] = ..., get_predicted_rate: bool = ..., get_lending_payments: bool = ..., get_borrow_rates: bool = ..., get_borrow_costs: bool = ..., include_all_rates: bool = ..., calculate_offline: bool = ..., taker_fee_rate: _Optional[str] = ..., rates: _Optional[_Iterable[_Union[MarginRate, _Mapping]]] = ...) -> None: ...

class LendingPayment(_message.Message):
    __slots__ = ["payment", "size"]
    PAYMENT_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    payment: str
    size: str
    def __init__(self, payment: _Optional[str] = ..., size: _Optional[str] = ...) -> None: ...

class BorrowCost(_message.Message):
    __slots__ = ["cost", "size"]
    COST_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    cost: str
    size: str
    def __init__(self, cost: _Optional[str] = ..., size: _Optional[str] = ...) -> None: ...

class MarginRate(_message.Message):
    __slots__ = ["time", "market_borrow_size", "hourly_rate", "yearly_rate", "hourly_borrow_rate", "yearly_borrow_rate", "lending_payment", "borrow_cost"]
    TIME_FIELD_NUMBER: _ClassVar[int]
    MARKET_BORROW_SIZE_FIELD_NUMBER: _ClassVar[int]
    HOURLY_RATE_FIELD_NUMBER: _ClassVar[int]
    YEARLY_RATE_FIELD_NUMBER: _ClassVar[int]
    HOURLY_BORROW_RATE_FIELD_NUMBER: _ClassVar[int]
    YEARLY_BORROW_RATE_FIELD_NUMBER: _ClassVar[int]
    LENDING_PAYMENT_FIELD_NUMBER: _ClassVar[int]
    BORROW_COST_FIELD_NUMBER: _ClassVar[int]
    time: str
    market_borrow_size: str
    hourly_rate: str
    yearly_rate: str
    hourly_borrow_rate: str
    yearly_borrow_rate: str
    lending_payment: LendingPayment
    borrow_cost: BorrowCost
    def __init__(self, time: _Optional[str] = ..., market_borrow_size: _Optional[str] = ..., hourly_rate: _Optional[str] = ..., yearly_rate: _Optional[str] = ..., hourly_borrow_rate: _Optional[str] = ..., yearly_borrow_rate: _Optional[str] = ..., lending_payment: _Optional[_Union[LendingPayment, _Mapping]] = ..., borrow_cost: _Optional[_Union[BorrowCost, _Mapping]] = ...) -> None: ...

class GetMarginRatesHistoryResponse(_message.Message):
    __slots__ = ["rates", "total_rates", "sum_borrow_costs", "avg_borrow_size", "sum_lending_payments", "avg_lending_size", "latest_rate", "predicted_rate", "taker_fee_rate"]
    RATES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RATES_FIELD_NUMBER: _ClassVar[int]
    SUM_BORROW_COSTS_FIELD_NUMBER: _ClassVar[int]
    AVG_BORROW_SIZE_FIELD_NUMBER: _ClassVar[int]
    SUM_LENDING_PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    AVG_LENDING_SIZE_FIELD_NUMBER: _ClassVar[int]
    LATEST_RATE_FIELD_NUMBER: _ClassVar[int]
    PREDICTED_RATE_FIELD_NUMBER: _ClassVar[int]
    TAKER_FEE_RATE_FIELD_NUMBER: _ClassVar[int]
    rates: _containers.RepeatedCompositeFieldContainer[MarginRate]
    total_rates: int
    sum_borrow_costs: str
    avg_borrow_size: str
    sum_lending_payments: str
    avg_lending_size: str
    latest_rate: MarginRate
    predicted_rate: MarginRate
    taker_fee_rate: str
    def __init__(self, rates: _Optional[_Iterable[_Union[MarginRate, _Mapping]]] = ..., total_rates: _Optional[int] = ..., sum_borrow_costs: _Optional[str] = ..., avg_borrow_size: _Optional[str] = ..., sum_lending_payments: _Optional[str] = ..., avg_lending_size: _Optional[str] = ..., latest_rate: _Optional[_Union[MarginRate, _Mapping]] = ..., predicted_rate: _Optional[_Union[MarginRate, _Mapping]] = ..., taker_fee_rate: _Optional[str] = ...) -> None: ...

class GetOrderbookMovementRequest(_message.Message):
    __slots__ = ["exchange", "asset", "pair", "amount", "sell", "requires_rest_orderbook", "purchase"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    SELL_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_REST_ORDERBOOK_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    asset: str
    pair: CurrencyPair
    amount: float
    sell: bool
    requires_rest_orderbook: bool
    purchase: bool
    def __init__(self, exchange: _Optional[str] = ..., asset: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., amount: _Optional[float] = ..., sell: bool = ..., requires_rest_orderbook: bool = ..., purchase: bool = ...) -> None: ...

class GetOrderbookMovementResponse(_message.Message):
    __slots__ = ["nominal_percentage", "impact_percentage", "slippage_cost", "currency_bought", "bought", "currency_sold", "sold", "side_affected", "update_protocol", "full_orderbook_side_consumed", "start_price", "end_price", "no_slippage_occurred", "average_order_cost"]
    NOMINAL_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    IMPACT_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    SLIPPAGE_COST_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_BOUGHT_FIELD_NUMBER: _ClassVar[int]
    BOUGHT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_SOLD_FIELD_NUMBER: _ClassVar[int]
    SOLD_FIELD_NUMBER: _ClassVar[int]
    SIDE_AFFECTED_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    FULL_ORDERBOOK_SIDE_CONSUMED_FIELD_NUMBER: _ClassVar[int]
    START_PRICE_FIELD_NUMBER: _ClassVar[int]
    END_PRICE_FIELD_NUMBER: _ClassVar[int]
    NO_SLIPPAGE_OCCURRED_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_ORDER_COST_FIELD_NUMBER: _ClassVar[int]
    nominal_percentage: float
    impact_percentage: float
    slippage_cost: float
    currency_bought: str
    bought: float
    currency_sold: str
    sold: float
    side_affected: str
    update_protocol: str
    full_orderbook_side_consumed: bool
    start_price: float
    end_price: float
    no_slippage_occurred: bool
    average_order_cost: float
    def __init__(self, nominal_percentage: _Optional[float] = ..., impact_percentage: _Optional[float] = ..., slippage_cost: _Optional[float] = ..., currency_bought: _Optional[str] = ..., bought: _Optional[float] = ..., currency_sold: _Optional[str] = ..., sold: _Optional[float] = ..., side_affected: _Optional[str] = ..., update_protocol: _Optional[str] = ..., full_orderbook_side_consumed: bool = ..., start_price: _Optional[float] = ..., end_price: _Optional[float] = ..., no_slippage_occurred: bool = ..., average_order_cost: _Optional[float] = ...) -> None: ...

class GetOrderbookAmountByNominalRequest(_message.Message):
    __slots__ = ["exchange", "asset", "pair", "nominal_percentage", "sell", "requires_rest_orderbook"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    SELL_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_REST_ORDERBOOK_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    asset: str
    pair: CurrencyPair
    nominal_percentage: float
    sell: bool
    requires_rest_orderbook: bool
    def __init__(self, exchange: _Optional[str] = ..., asset: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., nominal_percentage: _Optional[float] = ..., sell: bool = ..., requires_rest_orderbook: bool = ...) -> None: ...

class GetOrderbookAmountByNominalResponse(_message.Message):
    __slots__ = ["amount_required", "currency_selling", "amount_received", "currency_buying", "start_price", "end_price", "average_order_cost", "side_affected", "approximate_nominal_slippage_percentage", "update_protocol", "full_orderbook_side_consumed"]
    AMOUNT_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_SELLING_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_BUYING_FIELD_NUMBER: _ClassVar[int]
    START_PRICE_FIELD_NUMBER: _ClassVar[int]
    END_PRICE_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_ORDER_COST_FIELD_NUMBER: _ClassVar[int]
    SIDE_AFFECTED_FIELD_NUMBER: _ClassVar[int]
    APPROXIMATE_NOMINAL_SLIPPAGE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    FULL_ORDERBOOK_SIDE_CONSUMED_FIELD_NUMBER: _ClassVar[int]
    amount_required: float
    currency_selling: str
    amount_received: float
    currency_buying: str
    start_price: float
    end_price: float
    average_order_cost: float
    side_affected: str
    approximate_nominal_slippage_percentage: float
    update_protocol: str
    full_orderbook_side_consumed: bool
    def __init__(self, amount_required: _Optional[float] = ..., currency_selling: _Optional[str] = ..., amount_received: _Optional[float] = ..., currency_buying: _Optional[str] = ..., start_price: _Optional[float] = ..., end_price: _Optional[float] = ..., average_order_cost: _Optional[float] = ..., side_affected: _Optional[str] = ..., approximate_nominal_slippage_percentage: _Optional[float] = ..., update_protocol: _Optional[str] = ..., full_orderbook_side_consumed: bool = ...) -> None: ...

class GetOrderbookAmountByImpactRequest(_message.Message):
    __slots__ = ["exchange", "asset", "pair", "impact_percentage", "sell", "requires_rest_orderbook"]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    IMPACT_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    SELL_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_REST_ORDERBOOK_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    asset: str
    pair: CurrencyPair
    impact_percentage: float
    sell: bool
    requires_rest_orderbook: bool
    def __init__(self, exchange: _Optional[str] = ..., asset: _Optional[str] = ..., pair: _Optional[_Union[CurrencyPair, _Mapping]] = ..., impact_percentage: _Optional[float] = ..., sell: bool = ..., requires_rest_orderbook: bool = ...) -> None: ...

class GetOrderbookAmountByImpactResponse(_message.Message):
    __slots__ = ["amount_required", "currency_selling", "amount_received", "currency_buying", "start_price", "end_price", "average_order_cost", "side_affected", "approximate_impact_slippage_percentage", "update_protocol", "full_orderbook_side_consumed"]
    AMOUNT_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_SELLING_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_BUYING_FIELD_NUMBER: _ClassVar[int]
    START_PRICE_FIELD_NUMBER: _ClassVar[int]
    END_PRICE_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_ORDER_COST_FIELD_NUMBER: _ClassVar[int]
    SIDE_AFFECTED_FIELD_NUMBER: _ClassVar[int]
    APPROXIMATE_IMPACT_SLIPPAGE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    FULL_ORDERBOOK_SIDE_CONSUMED_FIELD_NUMBER: _ClassVar[int]
    amount_required: float
    currency_selling: str
    amount_received: float
    currency_buying: str
    start_price: float
    end_price: float
    average_order_cost: float
    side_affected: str
    approximate_impact_slippage_percentage: float
    update_protocol: str
    full_orderbook_side_consumed: bool
    def __init__(self, amount_required: _Optional[float] = ..., currency_selling: _Optional[str] = ..., amount_received: _Optional[float] = ..., currency_buying: _Optional[str] = ..., start_price: _Optional[float] = ..., end_price: _Optional[float] = ..., average_order_cost: _Optional[float] = ..., side_affected: _Optional[str] = ..., approximate_impact_slippage_percentage: _Optional[float] = ..., update_protocol: _Optional[str] = ..., full_orderbook_side_consumed: bool = ...) -> None: ...
