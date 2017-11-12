from {{cookiecutter.project_slug}} import world


def test_world():
    response = world.invoke({}, {})
    assert response == "Hello World"
