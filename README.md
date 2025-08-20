### installer

para continuar con la ejecucion de el proyecto conforme lo dejaste es tan cimple como ejecutar una serie de comandos que te ayudaran con la inicializacion de el projecto en cualquier dispocitivo.

para esto primero debes de ejecutar el comando para la creacion de el servidor interno e instalador de las carpetas venv.

para esto debes dirigirte a la carpeta contenedora del projecto `cd ////`.
una vez en esta carpeta contenedora ejecutas el comando:

```
python -m venv venv
```

y a su vez se debe de activar el entorno con el comando:

```
.\venv\Scripts\Activate
```

**nota:** recuerda que para esto es primordial encontrarse en la carpeta donde instalaste el venv la cual deverida de ser la principal que nos da acceso al backend y frontend

**una ves ejecutes estos comandos es importante que ejecutes la instalacion de las dependencias.**

para esto es primordial el uso del .txt que debe conterner el proyecto con las dependencias para su instalacion, para esto ejecuta el comando:

```
pip install -r requirements.txt
```

si esto no es pocible por la falta de la existencia del archivo .txt es primordial que se ejecute la instalacion manual de las dependencias con este comando:

```
pip install fastapi uvicorn psycopg2-binary sqlalchemy alembic python-dotenv
```

una ves instaladas todas las dependencias puedes ejecutar el comando:

```
pip freeze > requirements.txt
```

lo que creara el archivo con las dependencias que instalaste para el funcionamiento de la aplicacion.

luego de toda esta ejecucion se revisa que el servidor conecte con este comando que avilitara una URL para la visualizacion de el projecto.

```
uvicorn backend.app.main:app --reload
uvicorn app.main:app --reload --app-dir backend
```
