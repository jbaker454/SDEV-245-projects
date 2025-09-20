Users = [
  "Silver",
  "Raider",
  "Test",
]

Permissions = [
  "Admin",
  "Member",
]

UserPermissionMap = {
  "Silver": Permissions[0],
  "Raider": Permissions[1],
  "Test": Permissions[1],
}

errors = [
  "User Not Found"
]

def determineUser():
  user = input("Input UserName here: ")
  return user

def validateUser(inputUser):
  for user in Users:
    if user == inputUser:
      return user
  return None

def getUserPermissions(user):
  permission = UserPermissionMap[user]
  return permission

def outputUserPermissions(user, permission):
  print(user, " is a ", permission)

def main():
  user = determineUser()
  if validateUser(user):
    permission = getUserPermissions(user)
    outputUserPermissions(user, permission)
  else:
    print(errors[0])

main()