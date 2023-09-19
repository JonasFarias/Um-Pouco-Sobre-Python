# -*- coding: cp1252 -*-
# Conversor de Bases Grafico.
from eagle import *
import base_convert


def executar(app, wid):
    num_original = app["valor_inicial"]
    base_original = app["base_inicial"]
    base_final = app["base_final"]
    app["valor_final"] = base_convert.any2any(num_original, base_original, base_final)


def limpar(app, wid):
    app["valor_inicial"] = ""
    app["valor_final"] = ""


App(
    title="Conversor de Bases",
    window_size=(250, 250),
    center=(
        Entry(id="valor_inicial", label="Numero Original:", editable=True, persistent=True),
        UIntSpin(id="base_inicial", label="Base Original:", value=2, min=2, max=36, step=1),
        UIntSpin(id="base_final", label="Base Desejada:", value=2, min=2, max=36, step=1),
        Entry(id="valor_final", label="Valor Final: ", editable=False, persistent=True),
    ),
    bottom=(
        Button(id="bCalcular", label="Calcular", callback=executar),
        Button(id="bLimpar", label="Limpar", callback=limpar),
    ),
)

run()