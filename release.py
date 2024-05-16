from os import popen
from typing import Iterable, Tuple

FIX = "FIX"
MINOR = "MINOR"
MAJOR = "MAJOR"


def recebe_melhoria() -> str:
    return input("Digite o tipo de melhoria efetuada: [fix|minor|major]")


def melhoria_eh_valida(melhoria: str, melhorias_suportadas: Iterable[str, ...]) -> bool:
    return melhoria.upper().strip() in melhorias_suportadas


def ler_versao_atual() -> Tuple[int, int, int]:
    with open("./__version__", "r") as f:
        versao_atual = f.read()

    major, minor, fix = versao_atual.split(".")
    major = int(major)
    minor = int(minor)
    fix = int(fix)

    return (major, minor, fix)


def incrementar_versao(melhoria: str, versao_atual: Tuple[int, int, int]) -> Tuple[int, int, int]:
    major, minor, fix = versao_atual
    if melhoria == FIX:
        fix = fix + 1

    if melhoria == MINOR:
        fix = 0
        minor = minor + 1

    if melhoria == MAJOR:
        fix = 0
        minor = 0
        major = major + 1

    return major, minor, fix


def escrever_nova_versao(nova_versao: Tuple[int, int, int]):
    with open("./__version__", "w") as f:
        f.write(str_versao(nova_versao))


def str_versao(versao: Tuple[int, int, int]) -> str:
    major, minor, fix = versao
    return f"{major}.{minor}.{fix}"


if __name__ == '__main__':
    melhoria = recebe_melhoria()
    melhorias_suportadas = (FIX, MINOR, MAJOR)

    if not melhoria_eh_valida(melhoria, melhorias_suportadas):
        print(f"A melhoria digitada '{melhoria}' não é suportada.")
        exit(1)

    versao_atual = ler_versao_atual()
    nova_versao = incrementar_versao(melhoria, versao_atual)
    escrever_nova_versao(nova_versao)
    popen(f"sh ./release.sh {str_versao(nova_versao)}")
