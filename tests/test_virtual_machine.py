from virtual_machine.virtual_machine import *
import io
from unittest import mock
from unittest.mock import patch

def test_load(): 
    with mock.patch('sys.stdout', new=io.StringIO()) as printout:
        D = ["test"]
        I = ["load", "0", "print"]
        calc(D, I)
    assert printout.getvalue() == 'test\n'
    
def test_dup(): 
    with mock.patch('sys.stdout', new=io.StringIO()) as printout:
        D = ["test"]
        I = ["load", "0", "dup", "print", "print"]
        calc(D, I)  
    assert printout.getvalue() == 'test\ntest\n'
    
def test_add_two(): 
    with mock.patch('sys.stdout', new=io.StringIO()) as printout:
        D = [2, 3]
        I = ["load", "0", "load", "1", "add_two", "print"]
        calc(D, I)
    assert printout.getvalue() == '5\n'
    
def test_mul_two(): 
    with mock.patch('sys.stdout', new=io.StringIO()) as printout:
        D = [2, 3]
        I = ["load", "0", "load", "1", "mul_two", "print"]
        calc(D, I)
    assert printout.getvalue() == '6\n'
    
def test_mod_two(): 
    with mock.patch('sys.stdout', new=io.StringIO()) as printout:
        D = [7, 4]
        I = ["load", "0", "load", "1", "mod_two", "print"]
        calc(D, I)
    assert printout.getvalue() == '3\n'
    
def test_toint(): 
    with mock.patch('sys.stdout', new=io.StringIO()) as printout:
        D = [2, "3"]
        I = ["load", "0", "load", "1", "toint", "add_two", "print"]
        calc(D, I)
    assert printout.getvalue() == '5\n'
    
def test_jump(): 
    with mock.patch('sys.stdout', new=io.StringIO()) as printout:
        D = [1, 2, 3, 4, 5]
        I = ["load", "0", "jump", "6", "load", "1", "print"]
        calc(D, I)
    assert printout.getvalue() == '1\n'
    
def test_jump_if(): 
    with mock.patch('sys.stdout', new=io.StringIO()) as printout:
        D = [1, 2, 3, 4, 5]
        I = ["load", "0", "jump_if", "5", "7", "load", "1", "print"]
        calc(D, I)
        assert printout.getvalue() == '1\n'
     
    with mock.patch('sys.stdout', new=io.StringIO()) as printout:
        D = [0, 2, 3, 4, 5]
        I = ["load", "0", "jump_if", "5", "7", "load", "1", "print"]
        calc(D, I)
        assert printout.getvalue() == '2\n'