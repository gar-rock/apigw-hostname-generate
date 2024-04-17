# apigw-hostname-generate

## Overview

This project generates a list of most probably AWS API Gateway hostnames. It's intended for research purposes to aid in identifying and understanding API Gateway endpoints.

## Motivation

API Gateway hostnames can sometimes be challenging to predict or enumerate, especially in large-scale environments or when dealing with complex naming conventions. This tool aims to provide a method for generating likely hostnames to assist researchers in exploring AWS infrastructure.

## Usage

1. **Installation**: Clone the repository to your local machine.

2. **Dependencies**: Ensure you have Python installed on your system. This project uses Python 3.x.

3. **Generating Hostnames**:
- Run the script to generate a list of 10 million API Gateway hostnames, which is then cutdown to the most probably 50% (~ 5 million) using regex

4. **Output**:
- The generated hostnames will be saved to a file named `api_gateway_endpoints.txt` in the project directory.

## Disclaimer

This project is provided for educational and research purposes only. Any usage of the generated hostnames for malicious or unauthorized activities is strictly prohibited. 

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues if you encounter any problems or have suggestions for improvements.

## License

This project is licensed under the [MIT License](LICENSE).

the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
