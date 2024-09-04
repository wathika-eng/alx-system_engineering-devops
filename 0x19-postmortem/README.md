## Postmortem: Service Outage on September 2, 2024

**Issue Summary**

Duration of the Outage:

September 2, 2024, 02:15 AM - 04:30 AM (UTC)

**Impact:**

During this period, our user authentication service was intermittently down, affecting approximately 40% of users. Users experienced login failures and inability to access secured areas of the application.

**Root Cause:**

The outage was caused by a misconfiguration in the database connection settings that led to intermittent connection failures and high latency issues.

**Timeline**

02:15 AM UTC - The issue was first detected by a monitoring alert indicating a high rate of failed login attempts.
02:20 AM UTC - An engineer noticed the issue through an internal dashboard and confirmed that the authentication service was experiencing errors.
02:30 AM UTC - Initial investigation focused on server logs and found no anomalies; suspected issues with application code.
02:45 AM UTC - Misleading investigation led to examining application code for recent changes, which was not the root cause.
03:00 AM UTC - Escalated to the database team when the problem persisted, suspecting a database connectivity issue.
03:30 AM UTC - The database team identified a misconfigured connection pool limit in the database settings.
03:45 AM UTC - Connection pool limit was adjusted, and the authentication service began to recover.
04:00 AM UTC - Monitored the system to ensure stability and confirmed that the issue was resolved.
04:30 AM UTC - Incident officially resolved and normal operations resumed.

## Root Cause and Resolution
**Root Cause:**

The root cause was a misconfiguration in the database connection pool settings, specifically, the connection pool limit was set too low. This led to connection throttling and intermittent failures in the authentication service.

**Resolution:**

The connection pool limit was adjusted to a higher value, which resolved the issue. Additional configuration was implemented to handle peak loads more effectively.

## Corrective and Preventative Measures
**Improvements Needed:**

Review and enhance configuration management to prevent similar misconfigurations.
Improve monitoring and alerting systems to better detect and diagnose connection issues.
Tasks to Address the Issue:

**Update Configuration Management:**

Review and update database connection settings and pool limits.
Implement automated configuration validation before deployment.
Enhance Monitoring:

Add specific monitoring for database connection metrics.
Set up alerts for connection pool exhaustion and latency issues.
Review and Test Procedures:

Conduct regular stress tests to ensure system stability under load.
Perform periodic configuration reviews and validation checks.
Documentation:

Document the incident and resolution steps for future reference.
Update the knowledge base with information on handling similar issues.

This postmortem outlines the steps taken to identify, address, and resolve the issue, and outlines measures to prevent future occurrences.