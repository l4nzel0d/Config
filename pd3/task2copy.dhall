let Group = Text

let Student = { age : Natural, group : Group, name : Text }

let groups : List Group =
      List/generate 24 (\(i : Natural) -> "ИКБО-${Natural/show (i + 1)}-20")

let student =
      \(age : Natural) -> \(group : Group) -> \(name : Text) -> 
      { age = age, group = group, name = name } : Student

let students : List Student =
      [ student 19 "ИКБО-4-20" "Иванов И.И."
      , student 18 "ИКБО-4-20" "Петров П.П."
      , student 18 "ИКБО-4-20" "Сидоров С.С."
      , student 19 "ИКБО-20-23" "Васильев Б.А."
      ]

let subject : Text = "Конфигурационное управление"

in { groups = groups, students = students, subject = subject }
