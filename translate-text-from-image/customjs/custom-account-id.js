const AWS = require('aws-sdk');

const sts = new AWS.STS(
    {
        credentials: new AWS.SharedIniFileCredentials({
            profile: 'social-media-automation'
        })
    
    }
);

module.exports.getAccountId = async () => {
  // Checking AWS user details
  const { Account } = await sts.getCallerIdentity().promise();
  return Account;
};