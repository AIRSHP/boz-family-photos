# Boz Family Photos

A small Mac app that backs up the photos you choose to the Boz family archive.

It only sends what you put in **one Photos album, called Boz Family Archive Sync.** Nothing else in your Photos library is touched.

[**Download the latest version**](https://github.com/AIRSHP/boz-family-photos/releases/latest/download/Boz-Family-Photos.zip) · Needs macOS 13 (Ventura) or newer, on any Mac.

---

## Install (about 5 minutes, once)

You need the two-part key Dustin gives you (a **key ID** and an **application key**). Keep it private.

1. **Download** the app with the link above. Open your Downloads folder and double-click **Boz-Family-Photos.zip**.
2. **Drag** **Boz Family Photos** into your **Applications** folder.
3. **Open it** from Applications. Your Mac says it can't check the app. Click **Done**.
4. **Allow it once:** open **System Settings → Privacy & Security**, scroll down to the line about Boz Family Photos, and click **Open Anyway**. Enter your Mac password, then click **Open**.
5. **Set Up** opens by itself:
   - **This Mac belongs to:** pick your name.
   - **Photos album:** leave it as **Boz Family Archive Sync**.
   - **B2 key ID** and **B2 application key:** paste the two parts from Dustin.
   - Click **Check and Save**. You should see **Ready**.
6. **Make the album:** open **Photos**, choose **File → New Album**, and name it exactly **Boz Family Archive Sync**.
7. Click the **photo icon** in the menu bar at the top of the screen and choose **Sync Now**. When your Mac asks about Photos, choose **Allow Full Access**.
8. In the same menu, turn on **Open at Login** so it keeps running after a restart.

That's it. You only do this once. Updates install themselves.

---

## Everyday use

**To back up a photo or video, add it to the Boz Family Archive Sync album.** That's the only step.

- In Photos, select photos, then right-click → **Add to → Boz Family Archive Sync**.
- On your iPhone this works too, if iCloud Photos is on and your Mac uses the same Apple Account. Add the photo to Boz Family Archive Sync on the phone, and your Mac picks it up.
- The app checks the album every 3 hours, when your Mac wakes up, and whenever you choose **Sync Now**. Your Mac has to be on and the app running (look for the photo icon in the menu bar).
- The first sync of a big album can take a while. It's fine to keep using your Mac.

**What gets saved:** each photo or video as it looks in Photos today. If you edited it, the edited version is saved. If you edit it again later, the new version is saved too, next to the old one.

**Removing is safe:** taking a photo out of the album, or deleting it from Photos, does **not** delete it from the family archive.

---

## The menu

Click the photo icon in the menu bar:

| You see | Means |
|---|---|
| **Last sync 3:10 PM: 120 of 120 safe in B2** | Everything in the album is backed up. |
| **Syncing 12 of 40…** | Working on it. |
| **2 items failed (see Show Log)** | Usually a slow iCloud download or a network drop. Choose **Sync Now** later. |
| **Last try … failed** + a reason | See *Something's wrong* below. |
| **Version 0.2.0** | The version you have. |

The menu also has **Preview (no upload)**, which shows what would be sent without sending anything, plus **User Guide** (this page), **Check for Updates**, **Set Up…** and **Quit**.

---

## Updates

Updates install themselves. The app checks a couple of minutes after it starts, and then every 6 hours. It waits until a sync finishes, then restarts on the new version. You don't need to do anything, and your settings, key and Photos access carry over.

Before installing, the app checks that each update is signed with the family's own certificate. An update from anyone else is refused.

To check right away, choose **Check for Updates**.

---

## Something's wrong

| Message | What to do |
|---|---|
| **No album named "Boz Family Archive Sync"** | In Photos, make (or rename) an album to exactly **Boz Family Archive Sync**. |
| **2 albums are named "Boz Family Archive Sync"** | Rename the extra one. |
| **Photos access is limited / not granted** | **System Settings → Privacy & Security → Photos → Boz Family Photos → Full Access**. |
| **This B2 key can't be used** | The key is wrong or for someone else. Ask Dustin, then use **Set Up…** again. |
| **Open at Login could not be changed** | Move the app into **Applications**, open it from there, and try again. |
| **The app is running from a temporary location** | Move it into **Applications** and open it from there. |
| A box asks about **"Boz Family Photos B2 key"** | Enter your Mac password and click **Always Allow**. |
| No photo icon in the menu bar | Open **Boz Family Photos** from Applications. |

Still stuck? Choose **Show Log** and send Dustin a screenshot of the last few lines. The log never contains your key.

---

## What's new

### 0.2.1 (2026-11-10)
- The album is now called **Boz Family Archive Sync**, a name you won't use by accident. If you set up with the old name, Family Archive, just rename that album in Photos to Boz Family Archive Sync. The app switches over by itself, and nothing gets uploaded twice.

### 0.2.0 (2026-11-10)
- Updates now install themselves, and the app checks each one is signed by the family before installing it.
- New **User Guide** and **Check for Updates** items in the menu, and the version shows in the menu.
- Signed with the family certificate, so Photos access and your saved key carry over to new versions.

### 0.1.0 (2026-11-09)
- First version: backs up the Family Archive album to your own folder in the family archive. Nothing is ever deleted from the archive.
