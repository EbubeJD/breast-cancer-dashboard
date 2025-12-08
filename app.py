from fastapi import FastAPI
from dash import Dash
from starlette.middleware.wsgi import WSGIMiddleware

from layout import create_layout
from callbacks.overview import register_overview_callbacks
from callbacks.mrna import register_mrna_callbacks
from callbacks.mutation import register_mutation_callbacks
from callbacks.co import register_co_callbacks


# Create FastAPI app
app = FastAPI()


# ---- DASH APP SETUP ---- #
dash_app = Dash(
    __name__,
    requests_pathname_prefix="/dashboard/",
    suppress_callback_exceptions=True
)

dash_app.layout = create_layout()

# Register callbacks
register_overview_callbacks(dash_app)
register_mrna_callbacks(dash_app)
register_mutation_callbacks(dash_app)
register_co_callbacks(dash_app)

# Mount Dash inside FastAPI
app.mount("/dashboard", WSGIMiddleware(dash_app.server))



