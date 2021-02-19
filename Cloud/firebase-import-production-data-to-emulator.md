# Import Firestore data to local emulator

```sh
firebase login
gcloud auth login

firebase projects:list
firebase use your-project-name
gcloud projects list
gcloud config set project your-project-name

gcloud firestore export gs://your-project-name.appspot.com/your-choosen-folder-name

cd functions
gsutil -m cp -r gs://your-project-name.appspot.com/your-choosen-folder-name .

firebase emulators:start — import ./your-choosen-folder-name
```

```sh
#Stop following command execution if command before failed
set -e

#Remove previous bucket if exists
delete_previous_version_if_exists() {
  #We either delete local folder and bucket object or just a bucket
  rm -r ./your-choosen-folder &&
  gsutil -m rm -r gs://your-production-project/your-choosen-folder ||
  gsutil -m rm -r gs://your-production-project/your-choosen-folder
}

export_production_firebase_to_emulator() {
  #Export production firebase to emulator bucket
  gcloud firestore export gs://your-production-project/your-choosen-folder
  
  #Copy to local folder
  gsutil -m cp -r gs://your-production-project/your-choosen-folder .
}

#Run bash functions, either delete previous bucket and local folder if exists for update or just export clean way
delete_previous_version_if_exists && export_production_firebase_to_emulator ||
export_production_firebase_to_emulator
```


[https://stackoverflow.com/a/62977147](https://stackoverflow.com/a/62977147)
[https://medium.com/firebase-developers/how-to-import-production-data-from-cloud-firestore-to-the-local-emulator-e82ae1c6ed8](https://medium.com/firebase-developers/how-to-import-production-data-from-cloud-firestore-to-the-local-emulator-e82ae1c6ed8)
