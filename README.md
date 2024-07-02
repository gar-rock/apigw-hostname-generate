# apigw-hostname-generate

## Overview

This project generates a list of most probably AWS API Gateway hostnames. It's intended for research purposes to aid in identifying and understanding API Gateway endpoints.

## Motivation

API Gateway hostnames can sometimes be challenging to predict or enumerate, especially in large-scale environments or when dealing with complex naming conventions. This tool aims to provide a method for generating likely hostnames to assist researchers in exploring AWS infrastructure.

## Usage

1. **Installation**: Clone the repository to your local machine.

2. **Dependencies**: Ensure you have Python installed on your system. This project uses Python 3.x.

3. **Generating Hostnames**:
- Run `generate.py` to generate a list of 10 million API Gateway hostnames, which is then cutdown to the most probably 50% (~ 5 million) using regex

4. **Output**:
- The generated hostnames will be saved to a file named `api_gateway_endpoints.txt` in the project directory.

![generate_api.gif](generate_api.gif)

Some example endpoints:
```
.
.
.
rj14mmob7v
nsuk1zyn7v
fx61n6jrff
ln3husey5n
cwj1oywpq9
7l8arbogfk
3uonjir95x
x4de8fbkb9
fdysb21bld
bdux6hll1y
klm8t8gusu
crt4jakqs6
wf2pv6h8ji
uvwx4q52oc
h7t4gyrv9n
6a5kjnwmej
cn3zig0nfa
d56lw6fotg
.
.
.
```

## Disclaimer

This project is provided for educational and research purposes only. Any usage of the generated hostnames for malicious or unauthorized activities is strictly prohibited. 

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues if you encounter any problems or have suggestions for improvements.

## License

This project is licensed under the [MIT License](LICENSE).
