#  Secure Communication Using RSA, SSL & Flask

This project demonstrates basic cryptographic concepts including RSA key generation, SSL certificate creation, HTTPS Flask server setup, and digital signing/verification using Python.

##  Outputs & Explanations

###  Output 1: RSA Key Pair Generation
The script `generate_keys.py` successfully created an RSA key pair. The private and public keys are saved in `private_key.pem` and `public_key.pem` files, which are essential for encryption, signing, and secure communication.

---

###  Output 2: SSL Certificate Generation
The script `generate_ssl.py` successfully created a self-signed SSL certificate and its corresponding private key. This certificate is used to enable HTTPS for secure communication in web applications.

---

###  Output 3: HTTPS Flask Server Running
The Flask app `secure_server.py` is running with HTTPS enabled using the generated SSL certificate. It’s accessible at `https://127.0.0.1:5000`. Flask also gives a warning that it's a development server, not recommended for production use.

---

###  Output 4: Browser Display
When visiting `https://127.0.0.1:5000` in the browser, it displays "Secure HTTPS Server!", confirming that the Flask route works correctly. The browser still shows “Not secure” because the SSL certificate is self-signed and not trusted by default.

---

###  Output 5: Data Signing
The script `sign_data.py` successfully signed the data using the private key. The resulting digital signature is saved in `signature.sig`, which ensures the integrity and authenticity of the data.

---

###  Output 6: Signature Verification
The script `verify_signature.py` successfully verified the digital signature using the public key. This confirms that the data has not been altered and is authentic.

---

##  Summary
This project covers:
- RSA Key Pair Generation
- SSL Certificate Creation
- HTTPS Server with Flask
- Data Signing & Verification

Each part demonstrates a key aspect of secure communication and cryptographic integrity.
