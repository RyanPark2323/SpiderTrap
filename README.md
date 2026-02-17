# Basic SpiderTrap Implementation

### How it Works

A Spider Trap is an ethical hacking tool designed to trap malicious web crawlers. There are two main components that make up the trap. Firstly, in the robots.txt file, I have disallowed web crawlers from accessing a generic /system-logs-archive/. An ethical web crawler will respect that and ignore the path, sorting ethical from malicious web crawlers. Then, if the path is accessed, the trap is activated and the bot will access a recursivly generated directory listing. For every link the bot attempts to scrape, 10 new unqiue links will be generated. This will trap the bot in a infinite loop and waste it's resources trying to scrape it.

### How to Run the SpiderTrap

This implementation was built using the Flask Framework:

1. Clone the Repo:              Download the project files to your machine
2. Install Dependencies:        Ensure you have python installed, then run: pip install requirements.txt
3. Launch the Server:           Run: python app.py
4. Access Pages:                Landing Page: http://127.0.0.1:5000/ Trap: http://127.0.0.1:5000/system-logs-archive/

### Limitations

This is more of a Proof-of-Concept implementation. While it is effective against basic, greedy web scrapers that just ignore robots.txt is still has some specific limitations that should be addressed.

1. False Sense of Security: Advanced scrapers tend to have tech like loop-detection or path analyses that can identify recursive patterns and escape the trap. The current implementation will only work against more basic scrapers.
2. Resource Drain: This trap is designed to waste attacker resources, however, depending on how large the attack is, it could also consume a more than wanted amount of resources on the host. A more advanced trap would have ways to address this resource drag.
3. Static Logic: The current implementation uses a simple pattern based naming convention. A more sophistacted trap would probably have something like randomized file naming in order to evade signature-based detection measures that more modern scrapers will use.

### Ethical Considerations and Responsible Use

I think that this Spider Trap is very ethical and be used in a wide variety of siutations while stil being used responsibly. The nature of the trap means that there is really limited human impact. The landing page states the project's purpose and humans are also unable to get caught in the trap because they can just click away. We are also ensuring the saftey of public utility bots by having a standard robots.txt file which points away things like search engine indexers from the trap. This makes sure that ethical bots aren't trapped in the project. This also ensures that the trap will only activate for bots that specifically violate the access policy. Finally, there is no retailatory action by the trap, such as hacking back, it only wastes computer resources to discourage unauthorized scraping. 