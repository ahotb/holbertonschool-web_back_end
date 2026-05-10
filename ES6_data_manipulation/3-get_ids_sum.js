export default function getStudentIdsSum(){
	return students.reduce((acc, student) => acc + student.id, 0);
}