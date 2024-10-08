# Directory Brute Forcer v1.0

A simple Python tool to brute-force directories on a target website using a customizable wordlist.

This script allows penetration testers and bug bounty hunters to check for hidden or unlinked directories on a target web server.

---

## ⚙️ How to Use

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Vigil5153/Directory-Brute-Forcer.git
   ```

2. **Install the required dependencies**:
   This script requires `requests` to be installed. You can install it using:

   ```bash
   pip install requests
   ```

   Alternatively, install all dependencies from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script**:
   Run the script and provide the target URL and a wordlist (or use the default wordlist included in the repo):

   ```bash
   python brute_force.py
   ```

4. **Example Usage**:
   ```bash
   Enter the target URL (e.g., http://example.com): http://testphp.vulnweb.com
   Enter the path to your wordlist (default: wordlist.txt): wordlist2.txt - Or leave blank to use wordlist.txt
   ```

---

## 📝 Customizing the Wordlist

The tool comes with a default wordlist (`wordlist.txt`) which contains common directory names. You can modify this file or provide your own wordlist. Make sure each directory name is on a new line. Example entries:

```text
admin
login
dashboard
images
etc..
```

Simply edit the `wordlist.txt` file to suit your needs or point the tool to another wordlist file.

You can find the default wordlist [here](./wordlist.txt).

---

## 📄 Example Output

```bash
Starting directory brute force on: http://example.com
[+] Scan complete! Found directories:
[+] http://example.com/admin
[+] http://example.com/login
[-] No directories found or directories are hidden.
```

---

## 🚨 Important Notes:

- Make sure you have permission before testing any web servers.
- Use responsibly and ethically.

---

## 🤝 Contributions and Updates

- **Pull Requests**: Feel free to open a pull request if you want to contribute improvements, features, or fixes.
- **Issues**: Open an issue if you find bugs or want to request new features.
- **Updates**: This tool will be updated periodically. Stay tuned for new features and improvements.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
