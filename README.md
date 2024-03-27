# Flask as a dev container

Flask is WSGI web app framework written in Python. This app calculates sales commissions based on user input in a standard web browser.

## dev container

I'm using a dev container so I don't have to install Python and Flask on my Mac. All I need a is a Docker daemon, which in my case is `colima` and VS Code with the dev container extension.

## Known Issues

This dev container does not appear to start Flask as a `CMD` at the end of the Dockerfile, but as `postCreateCommand` in the `devcontainer.json` works.

If Flask does not start, manually start the flask app with this command run within the repo directory.

```bash
flask run --host=0.0.0.0
```

## Accessing the Flask app

Open a web browser and enter `localhost:5001` to see the Flask app

## Known Issues

In Coder's `envbuilder` project that leverages dev containers, lifecycle scripts in `devcontainer.json` like `postCreateCommand` and `postStartCommand` must redirect output to a file or `/dev/null` or the workspace hangs. Add `> /dev/null 2>&1` after any commands in those scripts.

## Resources

[Related repo with Coder envbuilder support](https://github.com/sharkymark/envb-flask-hw)

[Flask](https://flask.palletsprojects.com/)

[Dev Container specification](https://containers.dev/implementors/spec/)