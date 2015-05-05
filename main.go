// main.go
//
// Copyright 2015, Evan Prodromou <evan@e14n.com>
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//       http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package main

import (
    "fmt"
    "net/http"
    "encoding/json"
)

var users map[string]map[string]string

func userHandler(w http.ResponseWriter, r *http.Request) {
  nick := r.URL.Path[6:]
  fmt.Printf("Request for user %s\n", nick)
  user := users[nick]
  if user == nil {
    http.Error(w, "No such user", 404)
  } else {
    b, err := json.Marshal(user)
    marshalled := string(b)
    fmt.Printf("User: '%s'", marshalled)
    if err != nil {
      http.Error(w, "Error encoding data", 500)
    } else {
      w.Header().Set("Content-Type", "application/activitystreams+json")
      fmt.Fprintf(w, marshalled)
    }
  }
}

func main() {
  http.HandleFunc("/user/", userHandler)
  users = make(map[string]map[string]string)
  users["evan"] = map[string]string {
    "preferredUsername": "evan",
    "displayName": "Evan Prodromou",
    "summary": "A person",
    "icon": "https://e14n.com/uploads/evan/2014/9/24/knyf1g_thumb.jpg",
  }
  http.ListenAndServe(":8080", nil)
}
