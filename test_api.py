from mrecsys.utils.deploy import request_update
import socket
import argparse


def factorization_infer():
    # the return will be in bytes, so decode
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect(("localhost", 6000))

    data = {
        "service_name": "FACTORIZATION",
        "service_token": "98f6f754bd9840503459f832d4b243ba36351ec8",
        "data": {
            # "request": "rank_items",
            "request": "recommend",
            "inputs": {
                "user_id": "1000125153834388186",
                "selected_items": ["1023280480942069518",
                                   "306446194545434834",
                                   "3205701174830506022",
                                   "3217347275587941674"],
                "filter_items": ["6481221346259782889"]
            }
        }
    }
    soc.send(str(data).encode("utf8"))
    result_bytes = soc.recv(4096)
    result_string = result_bytes.decode("utf8")
    return "Result from server is {}".format(result_string)


def sequence_infer():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect(("localhost", 5000))

    data = {
        "service_name": "SEQUENCE",
        "service_token": "ee977806d7286510da8b9a7492ba58e2484c0ecc",
        "data": {
            "request": "rank_items",
            "inputs": {
                "sequence": ["100459171840484639", "100670421557790535"],
                "selected_items": ["1023280480942069518",
                                   "306446194545434834",
                                   "3205701174830506022",
                                   "3217347275587941674"],
                "filter_items": ["3217347275587941674"]
            }
        }
    }
    soc.send(str(data).encode("utf8"))
    result_bytes = soc.recv(4096)
    result_string = result_bytes.decode("utf8")
    return "Result from server is {}".format(result_string)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', '-m', help='define the model for testing api (factorization / sequence)')
    parser.add_argument('--request', '-r', help='define the request type (inference / update)')
    args = parser.parse_args()
    model = args.model
    request = args.request

    service_ip = "localhost"
    if model == 'factorization':
        service_port = 6000
        service_name = "FACTORIZATION"
        service_token = "98f6f754bd9840503459f832d4b243ba36351ec8"
        infer = factorization_infer()

    elif model == 'sequence':
        service_port = 5000
        service_name = "SEQUENCE"
        service_token = "ee977806d7286510da8b9a7492ba58e2484c0ecc"
        infer = sequence_infer()
    else:
        raise ValueError("Unknown Model Type")

    if request == 'update':
        print(request_update(service_ip=service_ip,
                             service_port=service_port,
                             service_name=service_name,
                             service_token=service_token))

    elif request == 'inference':
        print(infer)
    else:
        raise ValueError("Unknown Request Type")