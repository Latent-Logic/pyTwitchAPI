#  Copyright (c) 2023. Lena "Teekeks" During <info@teawork.de>
"""
EventSub
--------

EventSub lets you listen for events that happen on Twitch.

All available EventSub clients runs in their own thread, calling the given callback function whenever an event happens.

Look at :ref:`eventsub-available-topics` to find the topics you are interested in.

Available Transports
====================

EventSub is available with different types of transports, used for different applications.

.. list-table::
   :header-rows: 1

   * - Transport Method
     - Use Case
     - Auth Type
   * - :doc:`twitchAPI.eventsub.webhook`
     - Server / Multi User
     - App Authentication
   * - :doc:`twitchAPI.eventsub.websocket`
     - Client / Single User
     - User Authentication


.. _eventsub-available-topics:

Available Topics and Callback Payloads
======================================

List of available EventSub Topics.

The Callback Payload is the type of the parameter passed to the callback function you specified in :const:`listen_`.

.. list-table::
   :header-rows: 1

   * - Topic
     - Subscription Function & Callback Payload
     - Description
   * - **Channel Update** v1
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_update()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelUpdateEvent`
     - A broadcaster updates their channel properties e.g., category, title, mature flag, broadcast, or language.
   * - **Channel Update** v2
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_update_v2()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelUpdateEvent`
     - A broadcaster updates their channel properties e.g., category, title, content classification labels, broadcast, or language.
   * - **Channel Follow** v2
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_follow_v2()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelFollowEvent`
     - A specified channel receives a follow.
   * - **Channel Subscribe**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_subscribe()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelSubscribeEvent`
     - A notification when a specified channel receives a subscriber. This does not include resubscribes.
   * - **Channel Subscription End**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_subscription_end()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelSubscriptionEndEvent`
     - A notification when a subscription to the specified channel ends.
   * - **Channel Subscription Gift**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_subscription_gift()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelSubscriptionGiftEvent`
     - A notification when a viewer gives a gift subscription to one or more users in the specified channel.
   * - **Channel Subscription Message**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_subscription_message()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelSubscriptionMessageEvent`
     - A notification when a user sends a resubscription chat message in a specific channel.
   * - **Channel Cheer**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_cheer()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelCheerEvent`
     - A user cheers on the specified channel.
   * - **Channel Raid**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_raid()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelRaidEvent`
     - A broadcaster raids another broadcaster’s channel.
   * - **Channel Ban**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_ban()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelBanEvent`
     - A viewer is banned from the specified channel.
   * - **Channel Unban**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_unban()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelUnbanEvent`
     - A viewer is unbanned from the specified channel.
   * - **Channel Moderator Add**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_moderator_add()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelModeratorAddEvent`
     - Moderator privileges were added to a user on a specified channel.
   * - **Channel Moderator Remove**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_moderator_remove()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelModeratorRemoveEvent`
     - Moderator privileges were removed from a user on a specified channel.
   * - **Channel Points Custom Reward Add**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_points_custom_reward_add()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelPointsCustomRewardAddEvent`
     - A custom channel points reward has been created for the specified channel.
   * - **Channel Points Custom Reward Update**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_points_custom_reward_update()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelPointsCustomRewardUpdateEvent`
     - A custom channel points reward has been updated for the specified channel.
   * - **Channel Points Custom Reward Remove**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_points_custom_reward_remove()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelPointsCustomRewardRemoveEvent`
     - A custom channel points reward has been removed from the specified channel.
   * - **Channel Points Custom Reward Redemption Add**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_points_custom_reward_redemption_add()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelPointsCustomRewardRedemptionAddEvent`
     - A viewer has redeemed a custom channel points reward on the specified channel.
   * - **Channel Points Custom Reward Redemption Update**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_points_custom_reward_redemption_update()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelPointsCustomRewardRedemptionUpdateEvent`
     - A redemption of a channel points custom reward has been updated for the specified channel.
   * - **Channel Poll Begin**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_poll_begin()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelPollBeginEvent`
     - A poll started on a specified channel.
   * - **Channel Poll Progress**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_poll_progress()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelPollProgressEvent`
     - Users respond to a poll on a specified channel.
   * - **Channel Poll End**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_poll_end()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelPollEndEvent`
     - A poll ended on a specified channel.
   * - **Channel Prediction Begin**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_prediction_begin()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelPredictionEvent`
     - A Prediction started on a specified channel.
   * - **Channel Prediction Progress**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_prediction_progress()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelPredictionEvent`
     - Users participated in a Prediction on a specified channel.
   * - **Channel Prediction Lock**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_prediction_lock()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelPredictionEvent`
     - A Prediction was locked on a specified channel.
   * - **Channel Prediction End**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_prediction_end()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelPredictionEndEvent`
     - A Prediction ended on a specified channel.
   * - **Drop Entitlement Grant**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_drop_entitlement_grant()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.DropEntitlementGrantEvent`
     - An entitlement for a Drop is granted to a user.
   * - **Extension Bits Transaction Create**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_extension_bits_transaction_create()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ExtensionBitsTransactionCreateEvent`
     - A Bits transaction occurred for a specified Twitch Extension.
   * - **Goal Begin**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_goal_begin()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.GoalEvent`
     - A goal begins on the specified channel.
   * - **Goal Progress**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_goal_progress()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.GoalEvent`
     - A goal makes progress on the specified channel.
   * - **Goal End**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_goal_end()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.GoalEvent`
     - A goal ends on the specified channel.
   * - **Hype Train Begin**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_hype_train_begin()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.HypeTrainEvent`
     - A Hype Train begins on the specified channel.
   * - **Hype Train Progress**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_hype_train_progress()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.HypeTrainEvent`
     - A Hype Train makes progress on the specified channel.
   * - **Hype Train End**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_hype_train_end()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.HypeTrainEvent`
     - A Hype Train ends on the specified channel.
   * - **Stream Online**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_stream_online()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.StreamOnlineEvent`
     - The specified broadcaster starts a stream.
   * - **Stream Offline**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_stream_offline()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.StreamOfflineEvent`
     - The specified broadcaster stops a stream.
   * - **User Authorization Grant**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_user_authorization_grant()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.UserAuthorizationGrantEvent`
     - A user’s authorization has been granted to your client id.
   * - **User Authorization Revoke**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_user_authorization_revoke()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.UserAuthorizationRevokeEvent`
     - A user’s authorization has been revoked for your client id.
   * - **User Update**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_user_update()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.UserUpdateEvent`
     - A user has updated their account.
   * - **Channel Shield Mode Begin**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_shield_mode_begin()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ShieldModeEvent`
     - Sends a notification when the broadcaster activates Shield Mode.
   * - **Channel Shield Mode End**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_shield_mode_end()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ShieldModeEvent`
     - Sends a notification when the broadcaster deactivates Shield Mode.
   * - **Channel Charity Campaign Start**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_charity_campaign_start()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.CharityCampaignStartEvent`
     - Sends a notification when the broadcaster starts a charity campaign.
   * - **Channel Charity Campaign Progress**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_charity_campaign_progress()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.CharityCampaignProgressEvent`
     - Sends notifications when progress is made towards the campaign’s goal or when the broadcaster changes the fundraising goal.
   * - **Channel Charity Campaign Stop**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_charity_campaign_stop()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.CharityCampaignStopEvent`
     - Sends a notification when the broadcaster stops a charity campaign.
   * - **Channel Charity Campaign Donate**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_charity_campaign_donate()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.CharityDonationEvent`
     - Sends a notification when a user donates to the broadcaster’s charity campaign.
   * - **Channel Shoutout Create**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_shoutout_create()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelShoutoutCreateEvent`
     - Sends a notification when the specified broadcaster sends a Shoutout.
   * - **Channel Shoutout Receive**
     - Function: :const:`~twitchAPI.eventsub.base.EventSubBase.listen_channel_shoutout_receive()` |br|
       Payload: :const:`~twitchAPI.object.eventsub.ChannelShoutoutReceiveEvent`
     - Sends a notification when the specified broadcaster receives a Shoutout.

"""
