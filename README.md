# Web App to Encrypt and Decrypt RSA codes

[![Python Version](https://img.shields.io/badge/python-3.9.15-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.2.5-brightgreen.svg)](https://djangoproject.com)

The following web-app aims to encrypt and decrypt files using the RSA crypto-system.

## To encrypt a message code, one can:
Go to Encrypt. Upload the message code as a .txt file and press Encrypt. The application will encrypt the file, providing with a download link to the encrypted file. The key information will be displayed once the file is encrypted.

## To decrypt a ciphertext, one can:
Go to Decrypt. Upload the code as a .txt file, enter the public key and private key, and press Decrypt. The application will decrypt the file, providing with a download link to the decrypted file.

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/jdhruva03/fsRSA.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Apply the migrations:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.

## License

The source code is released under the [MIT License](https://github.com/jdhruva03/fsRSA/blob/master/LICENSE).