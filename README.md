# POROY - WebSocket RCE PoC

![Version](https://img.shields.io/badge/version-1.0-red)
![Python](https://img.shields.io/badge/python-3.x-blue)
![License](https://img.shields.io/badge/license-Educational-orange)

**Remote Code Execution Proof of Concept via WebSocket for eDEX-UI**

## ⚠️ Disclaimer

This tool is provided **for educational and security research purposes only**. Using this code against systems without explicit authorization is **illegal**. The author is not responsible for any malicious use.

## 📋 Description

POROY is a Proof of Concept demonstrating a Remote Code Execution (RCE) vulnerability in eDEX-UI through its WebSocket interface. The tool allows sending system commands and retrieving their output.

## 🎯 Vulnerability

eDEX-UI exposes a WebSocket interface that can be exploited to execute arbitrary system commands if accessible without proper authentication.

**CVE**: Not assigned  
**Affected Software**: eDEX-UI  
**Attack Vector**: WebSocket command injection

## 🔧 Requirements

- Python 3.x
- Required packages:
  ```bash
  pip install websocket-client colorama
  ```

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/S0cial-Lain/POROY.git
cd poroy

# Install dependencies
pip install websocket-client colorama
```

## 🚀 Usage

```bash
python poroy.py
```

The tool will prompt you for:
1. **Target WebSocket URL** (e.g., `ws://localhost:3000`)
2. **Command to execute** (e.g., `whoami`, `ls`, `dir`)

### Example

```
Target Websocket (e.g ws://localhost:3000) : ws://192.168.1.100:3000
Command To Send : whoami
Present day, Present Time...
Sending: whoami
Capturing output...
user@hostname
Done!
```

## 🔍 How It Works

1. Establishes a WebSocket connection to the target eDEX-UI instance
2. Sends the specified command with a carriage return (`\r`)
3. Captures and displays the command output
4. Closes the connection

## 🛡️ Detection & Mitigation

### For Security Teams
- Monitor WebSocket connections for suspicious activity
- Implement authentication on WebSocket endpoints
- Use network segmentation to limit eDEX-UI exposure

### For Users
- Do not expose eDEX-UI WebSocket interface to untrusted networks
- Use firewall rules to restrict access
- Update to the latest version if a patch is available

## 📝 Legal Notice

This tool is intended for:
- Authorized penetration testing
- Security research in controlled environments
- Educational purposes

**Unauthorized access to computer systems is illegal.** Always obtain proper authorization before testing.

## 🤝 Contributing

Contributions are welcome for:
- Bug fixes
- Feature improvements
- Documentation updates

Please submit pull requests or open issues on GitHub.

## 👤 Author

**S0cial_lain**

## 📄 License

This project is licensed for educational purposes only. Use responsibly.

## 🔗 References

- [eDEX-UI GitHub Repository](https://github.com/GitSquared/edex-ui)
- [WebSocket Security Best Practices](https://owasp.org/www-community/vulnerabilities/WebSocket_Security)

---

**Remember**: With great power comes great responsibility. Use this knowledge to make the internet safer, not to cause harm.
