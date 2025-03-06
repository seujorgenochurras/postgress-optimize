from typing import Any, Callable
from kink import di, inject  # type: ignore


def Injector[T](alias: Any | None = None) -> Callable[[type[T]], type[T]]:
    def decorator(class_type: type[T]) -> type[T]:
        return inject(alias=alias)(class_type)  # type: ignore

    return decorator


def Resolve[T](class_type: type[T]) -> Callable[[], T]:
    return lambda: di[class_type]
