Google Apps Script webhook to email orders to info.mahdev.lk@gmail.com

Steps to configure (quick):

1) Create a new Google Apps Script project (script.google.com).
2) Replace the default Code.gs content with the script below.
3) In the script, set the `TO_EMAIL` constant to `info.mahdev.lk@gmail.com`.
4) Deploy the script as a Web App: "Deploy > New deployment" → select "Web app" → Execute as: "Me" → Who has access: "Anyone" (or "Anyone with link"). Copy the Web App URL.
5) Open `server/mahdev.xml` in your theme and replace the placeholder `REPLACE_WITH_YOUR_SCRIPT_ID` in the form action with the path portion of your Web App URL (the full URL is fine).
6) Test by submitting the "Leave us a message" form; the script will email the form contents to the address.

Apps Script (paste into Code.gs):

function doPost(e) {
  var TO_EMAIL = 'info.mahdev.lk@gmail.com';
  try {
    var params = e.parameter || {};
    var name = params['entry.2005620554'] || params.name || '';
    var email = params['entry.1045781291'] || params.email || '';
    var phone = params['entry.1166974658'] || params.phone || '';
    var message = params['entry.839337160'] || params.message || '';

    var subject = 'New order / message from website';
    var body = '';
    body += 'Name: ' + name + '\n';
    body += 'Email: ' + email + '\n';
    body += 'Phone: ' + phone + '\n\n';
    body += 'Message:\n' + message + '\n\n';
    body += 'Received from: ' + (e && e.postData && e.postData.contents ? 'Form POST' : 'Unknown') + '\n';

    MailApp.sendEmail(TO_EMAIL, subject, body);
    return ContentService.createTextOutput(JSON.stringify({status: 'ok'})).setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({status: 'error', message: err.message})).setMimeType(ContentService.MimeType.JSON);
  }
}

Notes & alternatives:
- Google Apps Script sends email using the deployer account; make sure the deployer has permission and the account is active.
- If you prefer a third-party form-to-email provider (Formspree, Getform), replace the form `action` with the provider URL and follow their setup.
- For higher reliability and attachments support, a server-side endpoint or transactional email service (SendGrid/Mailgun) is recommended.

If you want, I can: 
- Add a mailto fallback for quick testing, and
- Update the theme with a tested Formspree example instead of Apps Script.
