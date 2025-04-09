import pytest
from cadastro import Cadastro
from verificar_cadastro_corrida import verificar_cadastro

def test_should_accept():
    cadastro1 = Cadastro(10, "infantil", 40, True)
    assert verificar_cadastro(cadastro1)

def test_should_not_accept_irregular_age():
    cadastro1 = Cadastro(9, "infantil", 40, True)
    assert not verificar_cadastro(cadastro1)

def test_should_not_accept_irregular_category():
    cadastro1 = Cadastro(10, "infanto-juvenil", 40, True)
    assert not verificar_cadastro(cadastro1)

def test_should_not_accept_irregular_time():
    cadastro1 = Cadastro(10, "infantil", 190, True)
    assert not verificar_cadastro(cadastro1)

def test_should_not_accept_irregular_sign():
    cadastro1 = Cadastro(10, "infantil", 40, False)
    assert not verificar_cadastro(cadastro1)

def test_should_not_accept_irregular_age_kids():
    cadastro1 = Cadastro(18, "infantil", 40, True)
    assert not verificar_cadastro(cadastro1)

def test_should_not_accept_irregular_age_junior():
    cadastro1 = Cadastro(18, "juvenil", 40, True)
    assert not verificar_cadastro(cadastro1)

def test_should_not_accept_irregular_age_senior():
    cadastro1 = Cadastro(15, "adulto", 40, True)
    assert not verificar_cadastro(cadastro1)



