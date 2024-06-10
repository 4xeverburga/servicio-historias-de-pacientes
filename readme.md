# Input:
Historia de paciente que es recopilada a traves de voz en la app.
Ocurre antes de que el usuario vaya a algun centro de prestacion de servicios medicos.

# Output
Se devuelve una lista de sintomas y de eventos extraidos de la historia del paciente.

# Proceso
Input->main.extraer_datos()
->src.construir_prompt()
->src.extractor()
->src.llm_connector()
->main.formatear_respuesta()
->
Output

