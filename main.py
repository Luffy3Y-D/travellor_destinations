from destinations.app import create_app

flaks_app = create_app()
flaks_app.app_context().push()
