from homework import take_from_list, calculate
import pytest
from filecmp import cmp

@pytest.mark.parametrize("i", ['a',"abc",[[4],[3], [12]],1.333])
def test_take_from_list_correct_type(i):
    with pytest.raises(ValueError, match=f"Indices should be integer or list of integers, not {type(i)}"):
        take_from_list([1,2,3],i)

def test_take_from_list_if_works_for_int():
    assert take_from_list([4,5,22,43,23],0) == [4]

def test_take_from_list_if_works_for_list():
    assert take_from_list([8,12,22,3221,3],[0,2]) == [8,22]

def test_calcule_file_in_d(tmp_path):
    f = tmp_path / "test_homework/output.json"
    f.parent.mkdir()
    f.touch()
    with pytest.raises(FileNotFoundError, match="No such file or directory: 'a.txt'"):
        calculate("a.txt", f)


def test_calculate(tmp_path):
    fo = tmp_path / "test_homework/output.json"
    fo.parent.mkdir()
    fo.touch()
    calculate("input.json", fo)
    assert cmp(fo, "output.json")