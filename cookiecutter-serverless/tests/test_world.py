from cookiecutter_serverless import world


def test_world():
    response = world.invoke({}, {})
    assert response == "Hello World"
