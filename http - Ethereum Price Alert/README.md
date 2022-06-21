# Crypto price Alert
### Aplicación de alerta de precio Crypto por medio de Alexa

Aplicación de alerta de precio Crypto por medio de Alexa

Esta aplicación utiliza la [API de coinmarketcap](https://coinmarketcap.com/api/documentation/v1/) para obtener el precio de una moneta, ethereum actualmente, cada minuto.

Si el precio pasa de 2 limites determinados da una alerta a un dispositivo Alexa usando la [API de voice monkey](https://voicemonkey.io/start).

### Requirements
- Python 3.9 or higher
- pip3 or higher
- pipenv installed
  - to install run:
  ```
  pip install pipenv
  ```
  [pipenv info](https://pypi.org/project/pipenv/)

## How to Use
  ```
  cd http - Ethereum Price Alert
  pipenv shell
  pipenv install
  ```

Es necesario registarse en ambas la [API de coinmarketcap](https://coinmarketcap.com/api/documentation/v1/) y la [API de voice monkey](https://voicemonkey.io/start) para obtener las llaves que te permitiran usarlas.

En el codigo encontraras varios valores encerrados <DE ESTA MANERA> por simbolos <>.

Cuando veas eso, es señal de que debes remplazarlo con tus propios valores.

una vez echo esto corre

```
python3 main.py
```
