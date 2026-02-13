import { Component, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-analyze',
  imports: [FormsModule],
  templateUrl: './analyze.html',
  styleUrl: './analyze.scss',
})
export class AnalyzeComponent {
  private selectedFile!: File;

  protected selectedRole!: string;
  protected loading = signal(false);
  protected result = signal<any | null>(null);

  protected onFileSelected(event: any): void {
    this.selectedFile = event.target.files[0];
  }

  protected analyze(): void {
    this.loading.set(true);

    setTimeout(() => {
      this.result.set({
        score: 76,
        feedback: 'Add more measurable achievements and include cloud technologies.',
        missingSkills: ["Docker", "AWS", "CI/CD"]
      });

      this.loading.set(false);
    }, 3000);
  }
}
