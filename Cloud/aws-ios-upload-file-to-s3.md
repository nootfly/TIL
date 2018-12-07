# iOS upload files to AWS S3

1. In info.plist, add AWS keys

   ```config
   	<key>AWS</key>
	<dict>
		<key>CredentialsProvider</key>
		<dict>
			<key>CognitoIdentity</key>
			<dict>
				<key>Default</key>
				<dict>
					<key>PoolId</key>
					<string>poolId</string>
					<key>Region</key>
					<string>US_WEST_2</string>
				</dict>
			</dict>
		</dict>
		<key>S3TransferUtility</key>
		<dict>
			<key>Default</key>
			<dict>
				<key>Region</key>
				<string>US_WEST_2</string>
			</dict>
		</dict>
	</dict>
   ```

2. Add configuration code in AppDelegate

   ```swift
       let credentialsProvider = AWSCognitoCredentialsProvider(regionType:.USWest2,identityPoolId: "poolId")
        let configuration = AWSServiceConfiguration(region:.USWest2, credentialsProvider:credentialsProvider)
        
        AWSServiceManager.default().defaultServiceConfiguration = configuration
   ```
3. Upload the file

   ```swift
   func uploadCSV(with data: Data) {
        let expression = AWSS3TransferUtilityUploadExpression()
        expression.progressBlock = progressBlock
        
        DispatchQueue.main.async(execute: {
            self.progressView.progress = 0
        })
        
        transferUtility.uploadData(
            data,
            bucket: "bucketName",
            key: "fileName",
            contentType: "text/csv",
            expression: expression,
            completionHandler: completionHandler).continueWith { (task) -> AnyObject? in
                if let error = task.error {
                    print("Error: \(error.localizedDescription)")
                }
                
                if let _ = task.result {
                    print("Upload Starting!")
                }
                return nil;
        }
   }
   ```