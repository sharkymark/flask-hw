# Flask as a dev container

Flask is WSGI web app framework written in Python. This app calculates sales commissions based on user input in a standard web browser.

## dev container

I'm using a dev container so I don't have to install Python and Flask on my Mac. All I need a is a Docker daemon, which in my case is `colima` and VS Code with the dev container extension.

## Coder env builder

This dev container has been modified to use the `postStartCommand` which is a lifecycle command that runs after the container is started and the dev container is built.  The `postStartCommand` is run in the background and the output is redirected to a log file with no hangup protection. The command is as follows:

```json
"postStartCommand": "flask run --host=0.0.0.0 --port 5001 > flask.log 2>&1"
```

Alternatively, consider starting Flask as a `CMD` in the Dockerfile

If the process ends and you want to start the flask app with this command run within the repo directory or use the command in `postStartCommand`.

```bash
flask run --host=0.0.0.0 --port 5001
```

> I use port 5001, since port 5000 on my Mac is used by an Apple service.

## Accessing the Flask app

Open a web browser and enter `localhost:5001` to see the Flask app

## Resources

[Flask](https://flask.palletsprojects.com/)

[Dev Container specification](https://containers.dev/implementors/spec/)
