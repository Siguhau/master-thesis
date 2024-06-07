# A Case Study on using GPT-4o for Broken Role-Based Access Control Vulnerability Detection

This repository is contains the implementation and collected data used in my Computer Science Master Thesis at the Norwegian University of Science and Technology (NTNU)

## Abstract

Broken Access Control (BAC) vulnerabilities are currently at the top of the OWASP Top 10 list of the most critical application security risks. Access Control policies like Role-Based Access Control (RBAC) are widely adopted mechanisms to restrict system access to authorized users, ensuring secure management of permissions in various applications. However, these mechanisms often have flaws, resulting in BAC.

Previous studies have predominantly focused on traditional automated tools for vulnerability detection, with some employing dynamic approaches using Large Language Models (LLMs) to detect vulnerabilities from requests. Additionally, there are studies exploring different prompt techniques on other types of vulnerabilities.

With the recent success of LLMs, there is potential for these models to contribute new insights to this field using appropriate prompt engineering techniques. This study aims to evaluate the effectiveness of utilizing LLMs, specifically the state-of-the-art model GPT-4 Omni (GPT-4o), to detect vulnerabilities in web applications with RBAC. The evaluation involves testing four different prompt engineering techniques on 12 web applications written in PHP and JSP.

This study seeks to answer the following research questions:
- **RQ1:** How effective are different prompting techniques when locating BAC vulnerabilities?
- **RQ2:** How effective is GPT-4o in detecting BAC vulnerabilities compared to traditional methods?
- **RQ3:** Can the application of GPT-4o reduce the time and resources required for vulnerability detection related to BAC?

Results indicate that the Zero Shot prompting technique is the most effective, demonstrating superior performance compared to other techniques tested. In-Context prompting with Random examples also shows promise. However, GPT-4o’s overall accuracy is lower than traditional methods, necessitating significant and costly manual validation.

While GPT-4o offers valuable insights that can enhance current detection methods, its accuracy challenges must be addressed before LLMs can be fully utilized for vulnerability detection in RBAC. Nonetheless, the potential benefits suggest that further research and development could make LLMs a viable tool in this domain.


## Usage

Feel free to use the contents of this repository, but note that if you want to test the implementation, you will need an OpenAI account with API access and a API Key.