# Copyright (C) 2015 Christopher Allan Webber <cwebber@dustycloud.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

###########################################################################
# Minipump Dootabase
#
# This is NOT a production ready database, by any means.  It's an
# in-memory "database" of a bunch of hashmaps.  This is *intentional*...
# minipump is not meant to be production code, but rather very simple
# to understand "minimal implementation" of the ActivityPump spec.
# And for a "database", what can be simpler than mutating dictionaries?
###########################################################################

ACTIVITIES = {}
USERS = {}
