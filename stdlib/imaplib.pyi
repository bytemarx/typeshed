import subprocess
import sys
import time
from _typeshed import Self
from socket import socket as _socket
from ssl import SSLContext, SSLSocket
from types import TracebackType
from typing import IO, Any, Callable, Pattern, TypeVar
from typing_extensions import Literal, TypeAlias

__all__ = ["IMAP4", "IMAP4_stream", "Internaldate2tuple", "Int2AP", "ParseFlags", "Time2Internaldate", "IMAP4_SSL"]

# TODO: Commands should use their actual return types, not this type alias.
#       E.g. Tuple[Literal["OK"], List[bytes]]
_CommandResults: TypeAlias = tuple[str, list[Any]]

_AnyResponseData: TypeAlias = list[None] | list[bytes | tuple[bytes, bytes]]

_T = TypeVar("_T")
_list: TypeAlias = list[_T]  # conflicts with a method named "list"

class IMAP4:
    error: type[Exception]
    abort: type[Exception]
    readonly: type[Exception]
    mustquote: Pattern[str]
    debug: int
    state: str
    literal: str | None
    tagged_commands: dict[bytes, _list[bytes] | None]
    untagged_responses: dict[str, _list[bytes | tuple[bytes, bytes]]]
    continuation_response: str
    is_readonly: bool
    tagnum: int
    tagpre: str
    tagre: Pattern[str]
    welcome: bytes
    capabilities: tuple[str, ...]
    PROTOCOL_VERSION: str
    if sys.version_info >= (3, 9):
        def __init__(self, host: str = ..., port: int = ..., timeout: float | None = ...) -> None: ...
        def open(self, host: str = ..., port: int = ..., timeout: float | None = ...) -> None: ...
    else:
        def __init__(self, host: str = ..., port: int = ...) -> None: ...
        def open(self, host: str = ..., port: int = ...) -> None: ...

    def __getattr__(self, attr: str) -> Any: ...
    host: str
    port: int
    sock: _socket
    file: IO[str] | IO[bytes]
    def read(self, size: int) -> bytes: ...
    def readline(self) -> bytes: ...
    def send(self, data: bytes) -> None: ...
    def shutdown(self) -> None: ...
    def socket(self) -> _socket: ...
    def recent(self) -> _CommandResults: ...
    def response(self, code: str) -> _CommandResults: ...
    def append(self, mailbox: str, flags: str, date_time: str, message: str) -> str: ...
    def authenticate(self, mechanism: str, authobject: Callable[[bytes], bytes | None]) -> tuple[str, str]: ...
    def capability(self) -> _CommandResults: ...
    def check(self) -> _CommandResults: ...
    def close(self) -> _CommandResults: ...
    def copy(self, message_set: str, new_mailbox: str) -> _CommandResults: ...
    def create(self, mailbox: str) -> _CommandResults: ...
    def delete(self, mailbox: str) -> _CommandResults: ...
    def deleteacl(self, mailbox: str, who: str) -> _CommandResults: ...
    def enable(self, capability: str) -> _CommandResults: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, t: type[BaseException] | None, v: BaseException | None, tb: TracebackType | None) -> None: ...
    def expunge(self) -> _CommandResults: ...
    def fetch(self, message_set: str, message_parts: str) -> tuple[str, _AnyResponseData]: ...
    def getacl(self, mailbox: str) -> _CommandResults: ...
    def getannotation(self, mailbox: str, entry: str, attribute: str) -> _CommandResults: ...
    def getquota(self, root: str) -> _CommandResults: ...
    def getquotaroot(self, mailbox: str) -> _CommandResults: ...
    def list(self, directory: str = ..., pattern: str = ...) -> tuple[str, _AnyResponseData]: ...
    def login(self, user: str, password: str) -> tuple[Literal["OK"], _list[bytes]]: ...
    def login_cram_md5(self, user: str, password: str) -> _CommandResults: ...
    def logout(self) -> tuple[str, _AnyResponseData]: ...
    def lsub(self, directory: str = ..., pattern: str = ...) -> _CommandResults: ...
    def myrights(self, mailbox: str) -> _CommandResults: ...
    def namespace(self) -> _CommandResults: ...
    def noop(self) -> tuple[str, _list[bytes]]: ...
    def partial(self, message_num: str, message_part: str, start: str, length: str) -> _CommandResults: ...
    def proxyauth(self, user: str) -> _CommandResults: ...
    def rename(self, oldmailbox: str, newmailbox: str) -> _CommandResults: ...
    def search(self, charset: str | None, *criteria: str) -> _CommandResults: ...
    def select(self, mailbox: str = ..., readonly: bool = ...) -> tuple[str, _list[bytes | None]]: ...
    def setacl(self, mailbox: str, who: str, what: str) -> _CommandResults: ...
    def setannotation(self, *args: str) -> _CommandResults: ...
    def setquota(self, root: str, limits: str) -> _CommandResults: ...
    def sort(self, sort_criteria: str, charset: str, *search_criteria: str) -> _CommandResults: ...
    def starttls(self, ssl_context: Any | None = ...) -> tuple[Literal["OK"], _list[None]]: ...
    def status(self, mailbox: str, names: str) -> _CommandResults: ...
    def store(self, message_set: str, command: str, flags: str) -> _CommandResults: ...
    def subscribe(self, mailbox: str) -> _CommandResults: ...
    def thread(self, threading_algorithm: str, charset: str, *search_criteria: str) -> _CommandResults: ...
    def uid(self, command: str, *args: str) -> _CommandResults: ...
    def unsubscribe(self, mailbox: str) -> _CommandResults: ...
    if sys.version_info >= (3, 9):
        def unselect(self) -> _CommandResults: ...

    def xatom(self, name: str, *args: str) -> _CommandResults: ...
    def print_log(self) -> None: ...

class IMAP4_SSL(IMAP4):
    keyfile: str
    certfile: str
    if sys.version_info >= (3, 9):
        def __init__(
            self,
            host: str = ...,
            port: int = ...,
            keyfile: str | None = ...,
            certfile: str | None = ...,
            ssl_context: SSLContext | None = ...,
            timeout: float | None = ...,
        ) -> None: ...
    else:
        def __init__(
            self,
            host: str = ...,
            port: int = ...,
            keyfile: str | None = ...,
            certfile: str | None = ...,
            ssl_context: SSLContext | None = ...,
        ) -> None: ...
    host: str
    port: int
    sock: _socket
    sslobj: SSLSocket
    file: IO[Any]
    if sys.version_info >= (3, 9):
        def open(self, host: str = ..., port: int | None = ..., timeout: float | None = ...) -> None: ...
    else:
        def open(self, host: str = ..., port: int | None = ...) -> None: ...

    def read(self, size: int) -> bytes: ...
    def readline(self) -> bytes: ...
    def send(self, data: bytes) -> None: ...
    def shutdown(self) -> None: ...
    def socket(self) -> _socket: ...
    def ssl(self) -> SSLSocket: ...

class IMAP4_stream(IMAP4):
    command: str
    def __init__(self, command: str) -> None: ...
    host: str
    port: int
    sock: _socket
    file: IO[Any]
    process: subprocess.Popen[bytes]
    writefile: IO[Any]
    readfile: IO[Any]
    if sys.version_info >= (3, 9):
        def open(self, host: str | None = ..., port: int | None = ..., timeout: float | None = ...) -> None: ...
    else:
        def open(self, host: str | None = ..., port: int | None = ...) -> None: ...

    def read(self, size: int) -> bytes: ...
    def readline(self) -> bytes: ...
    def send(self, data: bytes) -> None: ...
    def shutdown(self) -> None: ...

class _Authenticator:
    mech: Callable[[bytes], bytes]
    def __init__(self, mechinst: Callable[[bytes], bytes]) -> None: ...
    def process(self, data: str) -> str: ...
    def encode(self, inp: bytes) -> str: ...
    def decode(self, inp: str) -> bytes: ...

def Internaldate2tuple(resp: str) -> time.struct_time: ...
def Int2AP(num: int) -> str: ...
def ParseFlags(resp: str) -> tuple[str, ...]: ...
def Time2Internaldate(date_time: float | time.struct_time | str) -> str: ...
