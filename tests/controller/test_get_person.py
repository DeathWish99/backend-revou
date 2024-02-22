from app.services.person_services import Person_service


def test_get_persons(test_app, mocker):
    mock_customer_data = [
        {
            "id": 22,
            "name": "rafly",
            "phone": 23
        },
    ]

    mocker.patch.object(Person_service, 'get_all_persons', return_value=mock_customer_data)

    with test_app.test_client() as client:
        response = client.get("/v1/persons/")

    assert response.status_code == 200