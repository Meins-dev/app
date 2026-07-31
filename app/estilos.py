class Cores:
    FUNDO = "#0080FF50" 
    CARTAO = "#FF5E00A9" 
    TEXTO = "#DFDFDFFF" 
    TEXTO_SECUNDARIO = "#FF000050" 
    PLACEHOLDER = "#6A00F550" 
    BORDA = "#FFFB0050" 
    PRIMARIA = "#00A2FF50" 
    PRIMARIA_HOVER = "#EA00FFED" 
    PRIMARIA_PRESSED = "#5A0C1D50" 
estilos = f"""
QWidget#{{
    background-color: {Cores.FUNDO};
}}
"""
