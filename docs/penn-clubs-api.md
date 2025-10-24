# Penn Clubs — API Endpoints (initial extract)

This document is a first-pass extraction of the public API endpoints exposed by the `pennlabs/penn-clubs` backend.

Source files used for extraction:
- `backend/pennclubs/urls.py`
- `backend/clubs/urls.py`

Notes:
- All endpoints are served under the `/api/` prefix (see `backend/pennclubs/urls.py`).
- This is an initial list—some endpoints may have additional query params, nested ids, or alternative actions; further work should enumerate methods (GET/POST/PUT/PATCH/DELETE), sample requests, and serializer names.

## Top-level router resources (registered via DRF routers)

- /api/clubs/ — ClubViewSet (list, retrieve, create, update, delete)
- /api/clubfairs/ — ClubFairViewSet
- /api/events/ — EventViewSet
- /api/tags/ — TagViewSet
- /api/classifications/ — ClassificationViewSet
- /api/badges/ — BadgeViewSet
- /api/categories/ — CategoryViewSet
- /api/designations/ — DesignationViewSet
- /api/eligibilities/ — EligibilityViewSet
- /api/favorites/ — FavoriteViewSet
- /api/subscriptions/ — SubscribeViewSet
- /api/clubvisits/ — ClubVisitViewSet
- /api/searches/ — SearchQueryViewSet
- /api/memberships/ — MembershipViewSet
- /api/requests/membership/ — MembershipRequestViewSet
- /api/requests/ownership/ — OwnershipRequestViewSet
- /api/tickets/ — TicketViewSet
- /api/schools/ — SchoolViewSet
- /api/majors/ — MajorViewSet
- /api/student_types/ — StudentTypeViewSet
- /api/reports/ — ReportViewSet
- /api/years/ — YearViewSet
- /api/types/ — TypeViewSet
- /api/statuses/ — StatusViewSet
- /api/group_activity_options/ — GroupActivityOptionViewSet
- /api/users/ — UserViewSet
- /api/cycles/ — WhartonCyclesView
- /api/whartonapplications/ — WhartonApplicationAPIView
- /api/submissions/ — ApplicationSubmissionUserViewSet
- /api/templates/ — ClubApprovalResponseTemplateViewSet
- /api/booths/ — ClubBoothsViewSet

## Nested resources

Clubs nested resources (pattern: `/api/clubs/{club_pk}/...`):
- /api/clubs/{club_pk}/members/ — MemberViewSet (club members)
- /api/clubs/{club_pk}/events/ — ClubEventViewSet (events for a club)
- /api/clubs/{club_pk}/invites/ — MemberInviteViewSet
- /api/clubs/{club_pk}/assets/ — AssetViewSet
- /api/clubs/{club_pk}/notes/ — NoteViewSet
- /api/clubs/{club_pk}/testimonials/ — TestimonialViewSet
- /api/clubs/{club_pk}/questions/ — QuestionAnswerViewSet
- /api/clubs/{club_pk}/membershiprequests/ — MembershipRequestOwnerViewSet
- /api/clubs/{club_pk}/ownershiprequests/ — OwnershipRequestManagementViewSet
- /api/clubs/{club_pk}/advisors/ — AdvisorViewSet
- /api/clubs/{club_pk}/applications/ — ClubApplicationViewSet
- /api/clubs/{club_pk}/adminnotes/ — AdminNoteViewSet

Applications nested resources (pattern: `/api/clubs/{club_pk}/applications/{application_pk}/...`):
- /api/clubs/{club_pk}/applications/{application_pk}/questions/ — ApplicationQuestionViewSet
- /api/clubs/{club_pk}/applications/{application_pk}/submissions/ — ApplicationSubmissionViewSet
- /api/clubs/{club_pk}/applications/{application_pk}/extensions/ — ApplicationExtensionViewSet

Events nested resources:
- /api/events/{event_pk}/showings/ — EventShowingViewSet
- /api/clubs/{club_pk}/events/{event_pk}/showings/ — ClubEventShowingViewSet

Badges nested resources:
- /api/badges/{badge_pk}/clubs/ — BadgeClubViewSet

Other specific endpoints (function-based or explicit paths):
- /api/settings/ — UserUpdateAPIView (user settings)
- /api/settings/invites/ — EmailInvitesAPIView
- /api/settings/zoom/ — UserZoomAPIView
- /api/settings/zoom/meetings/ — MeetingZoomAPIView
- /api/settings/permissions/ — UserPermissionAPIView
- /api/settings/groups/ — UserGroupAPIView
- /api/settings/calendar_url/ — UserUUIDAPIView
- /api/favouriteevents/ — FavoriteEventsAPIView
- /api/calendar/{user_secretuuid}/ — FavoriteCalendarAPIView
- /api/emailpreview/ — email_preview view
- /api/scripts/ — ScriptExecutionView
- /api/options/ — OptionListView
- /api/webhook/meeting/ — MeetingZoomWebhookAPIView
- /api/whartonapplications/status/ — WhartonApplicationStatusAPIView
- /api/health/ — HealthView
- /api/settings/queue/ — RegistrationQueueSettingsView
- /api/settings/ranking-weights/ — RankingWeightsView
- /api/clubs/{club_code}/invite/ — MassInviteAPIView

## Next steps (recommended)
1. Expand each entry with: allowed HTTP methods, auth requirements, serializer names, request/response samples.
2. Auto-generate an OpenAPI (the backend exposes `/api/openapi/`) to cross-check endpoints and obtain schema details.
3. Add a short script or a small management task to dump endpoints and serializers automatically.

---

*This is a first-pass document created automatically from `backend/clubs/urls.py` and `backend/pennclubs/urls.py`. Please review and tell me any additions or changes you want before I open the PR.*
