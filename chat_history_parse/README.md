# Chat History Parse

The scripts are used to count the ocuurrence of certain words said by chat users in the chat history (in html form exported from Element Web).

---

## Data Observation

1. All the messages are contained within a `div` element with the class "mx_Export_EventWrapper".
2. Within a sequence of messages sent by one user and contained inside `<div class="mx_Export_EventWrapper">`, the `li` element of the first message has the class "mx_EventTile". Subsequent `li` elements have both "mx_EventTile" **and** "mx_EventTile_continuation" classes. 

    The first message format:
    ```html
    <div class="mx_Export_EventWrapper"> 
        <li class="mx_EventTile">
            <div class="mx_DisambiguatedProfile">
                <span class="mx_Username_color8 mx_DisambiguatedProfile_displayName" dir="auto">username</span>
            </div>
            <div class="mx_EventTile_avatar"
                <img src="users/user.png" style="width: 30px; height: 30px;" title="@user:server" alt="Avatar" data-testid="avatar-img" role="button" tabindex="0" class="mx_AccessibleButton mx_BaseAvatar mx_BaseAvatar_image">
            </div>
            <div class="mx_EventTile_line">
                <a href="https://matrix.to/#/!hash:server/xxx" aria-label="17:03">
                    <span class="mx_MessageTimestamp" title="Wed, May 17 2023 17:03:32" aria-hidden="true" aria-live="off">
                        17:03
                    </span>
                </a>
                <div class="mx_EventTile_e2eIcon mx_EventTile_e2eIcon_warning" aria-label="Encrypted by an unverified session">
                </div>
                <div class="mx_MTextBody mx_EventTile_content">
                    <span class="mx_EventTile_body" dir="auto">消息内容0</span>
                </div>
            </div>
        </li>
    </div>
    ```
    
    The second message format:

    ```html
    <div class="mx_Export_EventWrapper">
        <li class="mx_EventTile mx_EventTile_continuation">
            <div class="mx_EventTile_line">
                <a href="https://matrix.to/#/!hash:sever/xxx" aria-label="17:03">
                    <span class="mx_MessageTimestamp" title="Wed, May 17 2023 17:03:53" aria-hidden="true" aria-live="off">
                        17:03
                    </span>
                </a>
                <div class="mx_EventTile_e2eIcon mx_EventTile_e2eIcon_warning" aria-label="Encrypted by an unverified session">
                </div>
                <div class="mx_MTextBody mx_EventTile_content">
                    <span class="mx_EventTile_body" dir="auto">消息内容1</span>
                </div>
            </div>
        </li>
    </div>
    ```
