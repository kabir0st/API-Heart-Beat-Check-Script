# Server Status Checker

This Python script checks the status of various servers and sends a report to Discord via webhook. It evaluates the availability of specified URLs and alerts when a server is offline.

## Functionality

The script performs the following tasks:

1. Retrieves the current time in the Nepali time zone.
2. Checks the status of predefined servers by sending HTTP requests to their URLs.
3. Constructs a Discord embed message with server statuses.
4. Sends the message to a Discord channel through a webhook.

## Possible Pitfalls

1. **Dependency on External Services:** The script relies on external services, such as Discord webhooks and server URLs. Changes to these services' APIs or endpoints could cause the script to fail.

2. **Handling Connection Errors:** It may not handle all possible connection errors gracefully. For instance, it currently only catches `requests.ConnectionError`, but other network-related issues could occur.

3. **Limited Error Reporting:** The script provides minimal error reporting. Enhancing error handling and logging would improve its robustness and maintainability.

4. **Security Considerations:** Storing the webhook URL in the script may pose a security risk, especially if the script is shared or version-controlled publicly.


##Sample Discord Output:

![image](https://github.com/lurayy/API-Heart-Beat-Check-Script/assets/17372825/81b2f0e4-6382-4634-94e0-91e1da4aba02)

## If Server is Down
![image](https://github.com/lurayy/API-Heart-Beat-Check-Script/assets/17372825/0bae67ad-cab3-4025-bc9f-fba89e00a672)
