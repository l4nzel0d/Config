local groups = [
    "ИКБО-" + std.toString(i) + "-20"
    for i in std.range(1, 24)
];

local student(age, group, name) = {
    age: age,
    group: group,
    name: name,
};

local students = [
    student(19, "ИКБО-4-20", "Иванов И.И."),
    student(18, "ИКБО-4-20", "Петров П.П."),
    student(18, "ИКБО-4-20", "Сидоров С.С."),
    student(19, "ИКБО-20-23", "Васильев Б.А.")
];

{
    groups: groups,
    students: students,
    subject: "Конфигурационное управление"
}