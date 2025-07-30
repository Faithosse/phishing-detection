Instructions for AI-Powered Phishing Detection Script (Kali Linux)

Setup Environment:

Update and install tools:  sudo apt update && sudo apt install python3 python3-pip git -y


Install libraries:  pip3 install pandas numpy scikit-learn matplotlib seaborn --user


Verify:  python3 -c "import pandas, numpy, sklearn, matplotlib, seaborn; print('Libraries installed')"


Create directory:  mkdir -p /home/kali/phishing-detection && cd /home/kali/phishing-detection && git init


Optional: Take screenshots after each command using gnome-screenshot (save in /home/kali/phishing-detection/screenshots/).


Obtain Dataset:

Download:  wget https://labs-repos.iit.demokritos.gr/balab/mails.php -O phishing-2022.txt
mv phishing-2022.txt /home/kali/phishing-detection/


Optional: Take a screenshot after wget (save as screenshots/Dataset_download.png).


Write Script:

Create phishing_detector.py:  nano phishing_detector.py


Paste content from phishing_detector.py script.
Save and exit: Ctrl+O, Enter, Ctrl+X.
Optional: Take screenshots of the nano command and editor (save as screenshots/gnome-command.png and screenshots/script-gnome.png).


Run and Test Script:

Run:  python3 phishing_detector.py


Expected: Accuracy 1.00 on 15,140 samples, "Click here to claim your prize!" as Phishing.


Test function:  python3
>>> from phishing_detector import classify_email
>>> print(classify_email("Click here to claim your prize!"))


Expected: Phishing.


Optional: Take a screenshot of the output (save as screenshots/script-test.png).


Document Project:

Create this file:  nano INSTRUCTIONS.md


Paste these instructions.
Save and exit: Ctrl+O, Enter, Ctrl+X.
Upload:  git add INSTRUCTIONS.md
git commit -m "Add comprehensive instructions for Kali"
git push origin main


Optional: Take a screenshot after git push (save in screenshots/).
Suggestions: Clone with git clone https://github.com/Faithosse/phishing-detection.git and add legitimate emails.


Author: Faith Dennis Osse, connect on LinkedIn.

Future Improvements: Add legitimate emails, set up GitHub Actions, add visualizations.

