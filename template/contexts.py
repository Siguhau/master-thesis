def get_system_context():
    system_context = "I want you to act as a vulnerability detection system looking for broken access vulnerabilities."
    return system_context

def get_user_task():
    user_task = "Does the following code contain one of these bug types: CWE-22 Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') CWE-23 Relative Path Traversal CWE-35 Path Traversal: '.../...//' CWE-59 Improper Link Resolution Before File Access ('Link Following') CWE-200 Exposure of Sensitive Information to an Unauthorized Actor CWE-201 Exposure of Sensitive Information Through Sent Data CWE-219 Storage of File with Sensitive Data Under Web Root CWE-275 Permission Issues CWE-276 Incorrect Default Permissions CWE-284 Improper Access Control CWE-285 Improper Authorization CWE-352 Cross-Site Request Forgery (CSRF) CWE-359 Exposure of Private Personal Information to an Unauthorized Actor CWE-377 Insecure Temporary File CWE-402 Transmission of Private Resources into a New Sphere ('Resource Leak') CWE-425 Direct Request ('Forced Browsing') CWE-441 Unintended Proxy or Intermediary ('Confused Deputy') CWE-497 Exposure of Sensitive System Information to an Unauthorized Control Sphere CWE-538 Insertion of Sensitive Information into Externally-Accessible File or Directory CWE-540 Inclusion of Sensitive Information in Source Code CWE-548 Exposure of Information Through Directory Listing CWE-552 Files or Directories Accessible to External Parties CWE-566 Authorization Bypass Through User-Controlled SQL Primary Key CWE-601 URL Redirection to Untrusted Site ('Open Redirect') CWE-639 Authorization Bypass Through User-Controlled Key CWE-651 Exposure of WSDL File Containing Sensitive Information CWE-668 Exposure of Resource to Wrong Sphere CWE-706 Use of Incorrectly-Resolved Name or Reference CWE-862 Missing Authorization CWE-863 Incorrect Authorization CWE-913 Improper Control of Dynamically-Managed Code Resources CWE-922 Insecure Storage of Sensitive Information CWE-1275 Sensitive Cookie with Improper SameSite Attribute? Please answer Yes or No."
    return user_task

def get_cot_context():
    system_context = get_system_context()
    cot_context = "They are all related to Role-Based Access Control (RBAC)."
    return system_context + " " + cot_context

def get_cot_user_task():
    user_task = get_user_task()
    cot_tast = "Show each step of the process of identifying the bug type in the code."
    return user_task + " " + cot_tast