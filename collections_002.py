from typing import Collection, Iterable, List, TypeVar, Protocol, Generic

T = TypeVar("T")
V = TypeVar("V", covariant=True)

def find(collection: List[int], item: int) -> int:
    pass


def replace(collection: List[int], item: int, index: int) -> List[int]:
    pass


def find_any_type(collection: List[T], item: T) -> int:
    pass


def find_iterable(iterable: Iterable[T], item: T) -> int:
    pass


class IndexableCollection(Protocol, Generic[V]):
    def __getitem__(self, key: int) -> V:
        ...


def find_indexable(indexable: IndexableCollection[T], item: T) -> int:
    pass
