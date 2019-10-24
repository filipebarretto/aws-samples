'use strict'

class CreateDeploymentBucketPlugin {
  constructor(serverless, options) {
    this.serverless = serverless
    this.options = options
    this.provider = this.serverless.getProvider('aws')

    this.hooks = {
      'aws:common:validate:validate': this.onAWSValidate.bind(this)
    }
  }

  onAWSValidate() {
    // ignore if not deploy
    if (!this.serverless.processedInput.commands.includes('deploy')) {
      return
    }

    const bucketName = this.getBucketName()
    if (!bucketName) {
      this.serverless.cli.log(
        'No custom deployment bucket is set, nothing to create'
      )

      return
    }

    return this.bucketExists(bucketName)
      .then(exists => {
        if (exists) {
          this.serverless.cli.log(
            `"${bucketName}" bucket already exists, nothing to create`
          )

          return Promise.resolve()
        }

        return this.createBucket(bucketName)
          .then(() =>
            this.serverless.cli.log(`"${bucketName}" bucket was created`)
          )
      })
  }

  getBucketName() {
    return this.serverless
      .service
      .provider
      .deploymentBucket
  }

  bucketExists(bucketName) {
    return this.provider
      .request('S3', 'headBucket', { Bucket: bucketName })
      .then(() => true)
      .catch(() => false)
  }

  createBucket(bucketName) {
    return this.provider
      .request('S3', 'createBucket', { Bucket: bucketName })
  }
}

module.exports = CreateDeploymentBucketPlugin
