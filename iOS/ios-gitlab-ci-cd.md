# iOS GitLabe CI/CD


## Upload the project to Gitlab


## Setup Gitlab Runner

1.  Download Gitlab Runner on MacOS
    
    ```sh
    $ sudo curl — output /usr/local/bin/gitlab-runner https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-darwin-amd64

    sudo chmod +x /usr/local/bin/gitlab-runner

    ```

2. Register runner for your project and get your token from GitLab project CI/CD settings

    ```shell
    gitlab-runner register
    ```

## Install Fastlane and swiftlint

1. Prepare `Gemfile`

   ```shell
   source "https://rubygems.org"
   gem "fastlane"
   gem "cocoapods"
   gem "xcov"

   ```

2. Install `Fastlane` and initialize the project

   ```shell
   bundle install —-path vendor/bundle

   fastlane init
   ```

3. Cocoapod initialization and setup `SwiftLint` in your project according to [https://github.com/realm/SwiftLint](https://github.com/realm/SwiftLint)

   ```sh
   pod init

   pod 'SwiftLint'

   ```
4. Add lint lane and test lane to `Fastfile`

   ```yaml
   desc "Does a static analysis of the project. Configure the options in .swiftlint.yml"
    lane :lint do
    swiftlint(
    mode: :lint,
    executable: "Pods/SwiftLint/swiftlint",
    reporter: "html",
    output_file: "fastlane/swiftlint-results.html",
    config_file: '.swiftlint.yml',
    ignore_exit_status: true
    )
    end

    desc "Test an measure code coverage"
     lane :test do
     run_tests(devices: ["iPhone 11"])
     xcov(
     workspace: "Yourproject.xcworkspace",
     scheme: "yourschema",
     output_directory: "fastlane/xcov_output"
     )
     end
   ```

## Prepare CI/CD Pipeline

1. prepare `.gitlab-ci.yml` file

  ```yaml
   stages:
       - lint
       - unit_tests
   
   variables:
       LC_ALL: "en_US.UTF-8"
       LANG: "en_US.UTF-8"
   before_script:
       - bundle install --path vendor/bundle
       - bundle exec pod install
   lint:
       dependencies: []
       stage: lint
       script:
        - fastlane lint
       tags:
        - ios
   unit_tests:
       dependencies: []
       stage: unit_tests
       script:
        - fastlane test
       tags:
        - ios
  ```

2. Start Runner

   ```sh

   gitlab-runner start
   gitlab-runner run

   ```

3. Commit `.gitlab-ci.yml` changes and push it to Gitlab


## References

[https://medium.com/@phanquanghoang/using-gitlab-ci-cd-fastlane-for-ios-project-part-1-5e7db82a3566](https://medium.com/@phanquanghoang/using-gitlab-ci-cd-fastlane-for-ios-project-part-1-5e7db82a3566)

[https://medium.com/@phanquanghoang/https-medium-com-phanquanghoang-using-gitlab-ci-cd-fastlane-for-ios-project-part-2-f2c55bf6305e?](https://medium.com/@phanquanghoang/https-medium-com-phanquanghoang-using-gitlab-ci-cd-fastlane-for-ios-project-part-2-f2c55bf6305e?)


