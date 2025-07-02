from behave import __version__

def before_scenario(context, scenario):
    context.promotions = {}
