# secure-communication
Secure P2P communication, via public key exchange ([Diffie-Hellman key exchange](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)) and encryption algorithms.

## Background
This project is our [BMA](https://www.bms-zuerich.ch/schule/aktivitaeten/berufsmaturitaetsarbeiten) and a collaboartion betwean Andràs Horber and me (Till Studer).
The program is executed on the pocket calculators that we already need for class at our School, the TI-Nspire CX CAS.
The programming language we will use is what the TI-Nspire supports, i.e. either TI-Basic or Python 3. 
Our preference is Python 3, since it is more widespread than TI-Basic and we already have some experience with it. But it is currently (22.08.2020) unclear whether Python 3 will be supported by the TI-Nspire in time.

# Installation
1. clone the repo
2. create a virtual environment
`python -m venv .venv`
3. activate the virtual environment
- Windows: `.venv\Scripts\activate`
- Linux: `source ./.venv/bin/activate`
> To deactivate the venv type `deactivate`
4. update pip
`python -m pip install --upgrade pip`
5. install dependencies
`pip install -r requirements.txt`

## For Development
6. install the dev dependencies
`pip install -r requirements-dev.txt`